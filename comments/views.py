from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .models import Comment


@login_required
def comment_delete(request, id):
    obj = get_object_or_404(Comment, id=id)

    if obj.user != request.user:
        response = HttpResponse('У Вас недостаточно прав для удаления данного комментария')
        response.status_code = 403
        return response

    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        return HttpResponseRedirect(parent_obj_url)
    context = {
        "objects": obj,
    }
    return render(request, "comments/confirm_delete.html", context)


def comment_thread(request, id):
    obj = get_object_or_404(Comment, id=id)

    if not obj.is_parent:
        obj = obj.parent

    initial_data = {
        "content_type": obj.content_type,
        "object_id": obj.object_id,
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_content, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
            )
        return HttpResponseRedirect(new_content.content_object.get_absolute_url())

    context = {
            "comment": obj,
            "form": form,
    }

    return render(request, "comments/comment_thread.html", context=context)
