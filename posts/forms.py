from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False), label='Содержание')
    publish = forms.DateField(widget=forms.SelectDateWidget, label='Дата публикации')

    class Meta:
        model = Post
        fields = ["title",
                  "content",
                  "image",
                  "draft",
                  "publish"]
