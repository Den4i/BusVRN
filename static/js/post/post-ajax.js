// let like_outline_24 = "{% static \"like_outline_24.svg\" %})";
let like_active_24 = "{% static 'like_active_24.svg' %}";

$('#likes').click(function(){
    let postid = $(this).attr("data-postid");
    let like_count = $('#like_count');
    $.get('/like_post/', {post_id: postid}, function(data){
        like_count.css('background-image', 'url(' +like_active_24 + ')'
                        );
        console.log('url(' +like_active_24 + ')');
        // debugger;
        like_count.html(data);
    });
});