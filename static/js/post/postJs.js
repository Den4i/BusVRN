$('.comment-reply-btn').click(function (event) {
    event.preventDefault();
    if (event.defaultPrevented){
        $(this).parent().next('.comment-reply').fadeToggle();
    }
});

$('.content-markdown').each(function () {
    let content = $(this).text();
    let markedContent = marked(content);
    $(this).html(markedContent)
});

$('.content-markdown img').each(function () {
    $(this).addClass("img-responsive")
});

let contentInput = $('#id_content');

function setContent(value) {
    let markedContent = marked(value);
    $('#preview-content').html(markedContent);
    $('#preview-content img').each(function () {
        $(this).addClass("img-responsive")
    })
}

contentInput.keyup(function () {
    let newContent = $(this).val();
    setContent(newContent)
});

let titleInput = $('#id_title');

titleInput.keyup(function () {
    let newTitle = $(this).val();
    $('#preview-title').text(newTitle)
});