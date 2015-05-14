# Edx Xblock for video rating #
This Xblock allows rating videos and save the information in a MySQL database.

## Installation instructions ##
In order to install the XBlock into your Edx devstack Server you need to.

## Download the XBlock from github. Place the files inside your server.
##.   Install your block::
You must replace `/path/to/your/block` with the path where you have downloaded the xblock

        $ vagrant ssh
        vagrant@precise64:~$ sudo -u edxapp /edx/bin/pip.edxapp install /path/to/your/block

##. Create table in MySQL Server
    
    #.  Connect to your MySQL Server

    #.  Create table itemrating on your MySQL Server

        #   mysql db_name < item_rating.sql

##. Configure your MySQL connection in XBlock
    
    #.  Edit the file `/path/to/your/block/ratingvideo/settings.py`
    #.  Configure the correct values for 'user','password','host','database'
    #.  Save the changes

##.  Enable the block

    #.  In ``edx-platform/lms/envs/common.py``, uncomment:

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  In ``edx-platform/cms/envs/common.py``, uncomment:

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  In ``edx-platform/cms/envs/common.py``, change:

            'ALLOW_ALL_ADVANCED_COMPONENTS': False,

        to::

            'ALLOW_ALL_ADVANCED_COMPONENTS': True,

##.  Add the block to your courses advanced settings in Studio

    #. Log in to Studio, and open your course
    #. Settings -> Advanced Settings
    #. Change the value for the key ``"advanced_modules"`` to ``ratingvideo``


##.  Add your block into your course

    #. Edit a unit
    #. Advanced -> your-block

##. Deploying your XBlock

To deploy your block to your own hosted version of edx-platform, you need to install it
into the virtualenv where the platform is running on, and add to the list of ``ADVANCED_COMPONENT_TYPES``
in ``edx-platform/cms/djangoapps/contentstore/views/component.py``.

#. Using the XBlock in the course

.In the Studio go to:

![Settings->Advanced Settings](https://appedx.uc3m.es/images/p7.jpg)

.Add a ratingvideo policy key on the advanced_modules keys

![Settings->Advanced Settings](https://appedx.uc3m.es/images/p1.jpg)

.After that, a new button called Advanced will appear in your unit edit view

![Advanced](https://appedx.uc3m.es/images/p8.jpg)

.And a new option called ratingVideo. Which will add the component with the rating element to the course.

![Advanced](https://appedx.uc3m.es/images/p2.jpg)

.You can change the parameters of the ratingvideo xblock pressing the edit button. You can configure if you want to show the number of votes and the total score

![Edit](https://appedx.uc3m.es/images/p6.jpg)

.Right now you can change the id of video to rate.

![Edit](https://appedx.uc3m.es/images/p9.jpg)