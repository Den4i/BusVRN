from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    subject = forms.CharField(label='Тема обращения')
    feedtext = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 10}), label='Содержание')
    phone = PhoneNumberField(label='Контактный телефон')

    class Meta:
        model = Feedback
        fields = ["subject", "feedtext", "phone"]
