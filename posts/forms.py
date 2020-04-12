from django import forms
from pagedown.widgets import PagedownWidget
import datetime
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False), label='Содержание')
    publish = forms.DateField(widget=forms.SelectDateWidget, label='Дата публикации', initial=datetime.date.today)
    image = forms.FileField(widget=forms.FileInput, label='Изображение')
    draft = forms.BooleanField(widget=forms.CheckboxInput, label='Черновик', required=False)

    class Meta:
        model = Post
        fields = ["title",
                  "content",
                  "image",
                  "draft",
                  "publish"]
