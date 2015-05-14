/* Javascript for ratingXBlock. */
function ratingvideoXBlock(runtime, element) {

    function idSaved(result) {
        $('.idvideo', element).text(result.href);
    }

    $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.save-button').bind('click', function() {
        var data = {
            'idvideo': $(edit_idvideo).context.value,
            'showrating': $(edit_showrating).context.value,
            'showvotes': $(edit_showvotes).context.value
        };
        $('.xblock-editor-error-message', element).html();
        $('.xblock-editor-error-message', element).css('display', 'none');
        var handlerUrl = runtime.handlerUrl(element, 'save_id');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                window.location.reload(false);
            } else {
                $('.xblock-editor-error-message', element).html('Error: '+response.message);
                $('.xblock-editor-error-message', element).css('display', 'block');
            }
        });
    });

    if($(value_showvotes).context.value=='no')
    {
        console.log($("#edit_showvotes option")[1]);
        $($("#edit_showvotes option")[1]).prop('selected', true);
    }
    else
    {
        console.log($("#edit_showvotes option")[0]);
        $($("#edit_showvotes option")[0]).prop('selected', true);
    }
    if($(value_showrating).context.value=='no')
    {
        console.log($("#edit_showrating option")[1]);
        $($("#edit_showrating option")[1]).prop('selected', true);
    }
    else
    {
        console.log($("#edit_showrating option")[0]);
        $($("#edit_showrating option")[0]).prop('selected', true);
    }

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}

function ratingvideouserXBlock(runtime, element) {

    function commentSent(result) {
        $('.idvideo', element).text(result.href);
    }

    $(element).find('.erase-button').bind('click', function(e) {
    	e.preventDefault();
    	$(userscore).context.value = 0;
    	$(usercomment).context.value = 'Place your comment here';
    	html = '<div class="ec-stars-wrapper" style="float:left;">';
    	for(j=1;j<=5;j++)
        {
        	console.log('añado estrella para votar');
        	html+='<a href="#" class="star" data-value="'+j+'" title="Votar con '+j+' estrellas">&#9733;</a>';
        }
        html+='</div>';
        $(element).find("#ratingcontainer").html(html);
        runtime.notify('cancel', {});
    });

    $(element).find('.send-button').bind('click', function(e) {
    	e.preventDefault();
        var data = {
            'userscore': $(userscore).context.value,
            'usercomment': $(usercomment).context.value
        };

        $('.xblock-editor-error-message', element).html();
        $('.xblock-editor-error-message', element).css('display', 'none');
        var handlerUrl = runtime.handlerUrl(element, 'sendcomment');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                window.location.reload(false);
                alert('Your vote and comment was sucefully sended');
            } else {
                alert('Error: '+response.result);
            }
        });
    });

    $(element).find('#ratingcontainer').on('click','.star', function(e) {
    	e.preventDefault();
    	console.log(this);
    	value = $(this).attr('data-value');
        $(userscore).context.value = value;
        console.log('value: '+value);
        html='<div class="ec-starsselected-wrapper" style="float:left;">';
        for(i=0;i<value;i++)
        {
        	console.log('añado una estrella ya votada');
        	html+='<a href="#" class="star" data-value="'+(i+1)+'" title="Votado con '+(i+1)+' estrellas">&#9733;</a>';
        }
        html+='</div><div class="ec-stars-wrapper" style="float:left;">';
        for(j=i+1;j<=5;j++)
        {
        	console.log('añado estrella para votar');
        	html+='<a href="#" class="star" data-value="'+j+'" title="Votar con '+j+' estrellas">&#9733;</a>';
        }
        html+='</div>';
        $(element).find("#ratingcontainer").html(html);
    });

    $(function ($) {
        
    });
}

function videorateduserXBlock(runtime, element) {

	$(element).find('#ratingcontainer').on('click','.star', function(e) {
    	e.preventDefault();
    });

    $(function ($) {
        value = $(userscore).context.value;
        html='<div class="ec-starsselected-wrapper" style="float:left;">';
        for(i=0;i<value;i++)
        {
        	console.log('añado una estrella ya votada');
        	html+='<a href="#" class="star" data-value="'+(i+1)+'" title="Votado con '+(i+1)+' estrellas">&#9733;</a>';
        }
        html+='</div><div class="ec-stars-wrapper" style="float:left;">';
        for(j=i+1;j<=5;j++)
        {
        	console.log('añado estrella para votar');
        	html+='<a href="#" class="star" data-value="'+j+'" title="Votar con '+j+' estrellas">&#9733;</a>';
        }
        html+='</div>';
        $(element).find("#ratingcontainer").html(html);
    });
}