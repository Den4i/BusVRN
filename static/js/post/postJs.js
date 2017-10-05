$('.comment-reply-btn').click(function (event) {
    event.preventDefault();
    $(this).parent().next('.comment-reply').fadeToggle();
});

$('.content-markdown').each(function () {
    var content = $(this).text();
    var markedContent = marked(content);
    $(this).html(markedContent)
});

$('.content-markdown img').each(function () {
    $(this).addClass("img-responsive")
});

var contentInput = $('#id_content');

function setContent(value) {
    var markedContent = marked(value);
    $('#preview-content').html(markedContent);
    $('#preview-content img').each(function () {
        $(this).addClass("img-responsive")
    })
}

contentInput.keyup(function () {
    var newContent = $(this).val();
    setContent(newContent)
});

var titleInput = $('#id_title');
function setTitle(value) {
    $('#preview-title').text(value)
}

titleInput.keyup(function () {
    var newTitle = $(this).val();
    setTitle(newTitle)
});