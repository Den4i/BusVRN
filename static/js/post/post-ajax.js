$('#likes').click(function(){
    var postid;
    postid = $(this).attr("data-postid");
    $.get('/like_post/', {post_id: postid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});