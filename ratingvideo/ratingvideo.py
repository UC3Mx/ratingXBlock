# coding=utf-8
__author__ = u"David Santín"
__credits__ = u"David Santin"
__version__ = u"1.50-BETA"
__maintainer__ = u"David Santín"
__email__ = u"dsantin@di.uc3m.es"
__status__ = u"Development"

import pkg_resources
import datetime
import mysql.connector

# from xblock.fields import Integer, Scope, String, Any, Boolean, Dict
from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xmodule.fields import RelativeTime
from mysql.connector import errorcode
import settings as s

# Make '_' a no-op so we can scrape strings

class ratingXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    idvideo = String(display_name="idvideo",
                  default="enter Youtube id",
                  scope=Scope.content,
                  help="Youtube id video for rating")
    showrating = String(display_name="showrating",
                  default="yes",
                  scope=Scope.content,
                  help="Define if rating is showed to students")
    showvotes = String(display_name="showvotes",
                  default="yes",
                  scope=Scope.content,
                  help="Define if votes are showed to students")
    submissions_count = Integer(
        default=0, help="Number of times the user has sent a submission.", scope=Scope.user_state
    )
    userscore = String(
        default="0", help="Number of times the user has sent a submission.", scope=Scope.user_state
    )
    usercomment = String(
        default="Place your comment here", help="Number of times the user has sent a submission.", scope=Scope.user_state
    )
    ip = ""
    login = ""
    totalscore = 0
    votes = 0

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def insert_tupla(self,score,comment,ip,login):
        cnx = mysql.connector.connect(**s.database)
        cursor = cnx.cursor()
        data_comment = {
            'youtube_id': self.idvideo,
            'user': login,
            'rating': score,
            'comment': comment,
            'ip': ip,
            'creation_date': ''
        }
        add_comment = ("INSERT INTO item_rating "
              "(youtube_id, user, rating, comment,ip,creation_date) "
              "VALUES (%(youtube_id)s, %(user)s, %(rating)s, %(comment)s,%(ip)s,NOW())")
        cursor.execute(add_comment, data_comment)
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def student_id(self):
        return self.xmodule_runtime.anonymous_student_id

    def get_totalscore(self):
        if(self.idvideo == 'enter Youtube id'):
            return '--'
        else:
            score = 0
            cnx = mysql.connector.connect(**s.database)
            cursor = cnx.cursor()
            data_comment ={
                'youtube_id': self.idvideo
            }
            query = ("SELECT SUM(rating) FROM item_rating "
            "WHERE youtube_id = %(youtube_id)s")
            cursor.execute(query, data_comment)
            for (value) in cursor:
                sumscore = value[0]
            votes = self.get_totalvotes()
            if votes == '--':
                return '--'
            else:
                score = float(sumscore) / float(votes)
                scorestr = '%.2f' % score
                return scorestr

    def get_totalvotes(self):
        if(self.idvideo == 'enter Youtube id'):
            return '--'
        else:
            votes = 0
            cnx = mysql.connector.connect(**s.database)
            cursor = cnx.cursor()
            data_comment ={
                'youtube_id': self.idvideo
            }
            query = ("SELECT COUNT(*) FROM item_rating "
            "WHERE youtube_id = %(youtube_id)s")
            cursor.execute(query, data_comment)
            for (value) in cursor:
                votes = value[0]
            if int(votes)==0:
                return '--'
            else:
                return votes

    def get_last_date(self,ip):
        return

    @XBlock.json_handler
    def save_id(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        #assert data['hello'] == 'world'
        self.idvideo = data['idvideo']
        self.showrating = data['showrating']
        self.showvotes = data['showvotes']

        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def sendcomment(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        #assert data['hello'] == 'world'

        #Check if id is correct formatted
        if(self.idvideo == 'enter Youtube id'):
            return {
                'result':'You must set Id video',
            }
        else:
            self.submissions_count += 1
            if self.submissions_count > 1:
                return {
                    'result': 'forbidden',
                }   
            else:
                self.userscore = data['userscore']
                self.usercomment = data['usercomment']
                self.ip = 'unknown'
                self.login = self.student_id()
                self.insert_tupla(self.userscore,self.usercomment,self.ip,self.login)

                return {
                    'result': 'success',
                }

    def student_view(self, context=None):
        """
        The primary view of the paellainteractiveXBlock, shown to students
        when viewing courses.
        """

        self.totalscore = self.get_totalscore()
        self.votes = self.get_totalvotes()
        if self.submissions_count > 0:
            if self.showrating=='yes' and self.showvotes=='yes':
                html = self.resource_string("static/html/showrating_rv.html")
            elif self.showrating=='yes':
                html = self.resource_string("static/html/showrating_r.html")
            elif self.showvotes=='yes':
                html = self.resource_string("static/html/showrating_v.html")
            else:
                html = self.resource_string("static/html/showrating.html")
            frag = Fragment(html.format(self=self))
            frag.add_css(self.resource_string("static/css/style_rated.css"))
            frag.add_javascript(self.resource_string("static/js/src/ratingvideo.js"))
            frag.initialize_js('videorateduserXBlock')
            return frag
        else:
            if self.showrating=='yes' and self.showvotes=='yes':
                html = self.resource_string("static/html/ratingvideo_rv.html")
            elif self.showrating=='yes':
                html = self.resource_string("static/html/ratingvideo_r.html")
            elif self.showvotes=='yes':
                html = self.resource_string("static/html/ratingvideo_v.html")
            else:
                html = self.resource_string("static/html/ratingvideo.html")
            frag = Fragment(html.format(self=self))
            frag.add_css(self.resource_string("static/css/style.css"))
            frag.add_javascript(self.resource_string("static/js/src/ratingvideo.js"))
            frag.initialize_js('ratingvideouserXBlock')
            return frag

    # TO-DO: change this view to display your data your own way.
    def studio_view(self, context=None):
        """
        The primary view of the paellainteractiveXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/ratingvideo_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/ratingvideo.js"))
        frag.initialize_js('ratingvideoXBlock')
        return frag

    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ratingXBlock",
             """<vertical_demo>
                <ratingvideo/>
                </vertical_demo>
             """),
        ]