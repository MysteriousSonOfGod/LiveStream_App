from re import S
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.db.models import fields
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("올바르지 않은 패스워드입니다."))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("해당 유저가 존재하지 않습니다."))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "first_name",
            "last_name",
            "email",
            "gender",
        ]

    nickname = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        try:
            models.User.objects.get(nickname=nickname)
            raise forms.ValidationError("이미 사용 중인 닉네임입니다.")
        except models.User.DoesNotExist:
            return nickname

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("패스워드가 일치하지 않습니다.")
        else:
            return password

    def save(self):
        username = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = super().save(commit=False)
        user.username = username
        user.set_password(password)
        user.nickname = self.cleaned_data.get("nickname")
        user.save()
