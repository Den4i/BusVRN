from django import forms
from django.contrib.auth import (authenticate,
                                 get_user_model,
                                 login,
                                 logout)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Пользователь не существует")
            if not user.check_password(password):
                raise forms.ValidationError("Не верный пароль")
            if not user.is_active:
                raise forms.ValidationError("Пользователь не активирован")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Адрес эл. почты')
    email2 = forms.EmailField(label='Подтверждение')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'email2'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Эл. адреса не совпадают")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Такой почтовый адрес уже зарегистрирован")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
