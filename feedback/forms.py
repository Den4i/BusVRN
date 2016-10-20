from django import forms
from pagedown.widgets import PagedownWidget
from .models import FeedbackModel


class FeedbackForm(forms.ModelForm):
	subject = forms.CharField(widget=PagedownWidget(show_preview=False), label='Тема обращения')
	feedtext = forms.CharField(widget=PagedownWidget(show_preview=False), label='Содержание')
	phone = forms.CharField(label='Контактный телефон', max_length=11)

	class Meta:
		model = FeedbackModel
		fields = ["subject", "feedtext", "phone"]
