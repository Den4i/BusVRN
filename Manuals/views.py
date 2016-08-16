from django.shortcuts import render, get_object_or_404

from .models import Object


def index(request):
    object_list = Object.objects.all()
    context = {'object_list': object_list}
    return render(request, 'Manuals/index.html', context)


def detail(request, object_id):
    object = get_object_or_404(Object, pk=object_id)
    return render(request, 'Manuals/detail.html', {'object': object})