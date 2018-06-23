from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    subject = forms.CharField(label='Тема обращения')
    feedtext = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 10}), label='Содержание')
    phone = forms.CharField(label='Контактный телефон', max_length=11)

    class Meta:
        model = Feedback
        fields = ["subject", "feedtext", "phone"]
