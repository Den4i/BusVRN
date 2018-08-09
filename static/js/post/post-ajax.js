$('#likes').click(function(){
    let postid = $(this).attr("data-postid");
    let likes = $('#likes');
    $.get('/like_post/', {post_id: postid}, function(data){
        data.active === true ? likes.css('background-image', 'url('+like_active_24+')') :
                               likes.css('background-image', 'url('+like_outline_24+')');

        $('#like_count').html(data.likes);
    });
});