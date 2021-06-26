from users import forms
from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.urls.base import reverse
from django.urls import reverse_lazy
from . import forms


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):

    template_name = "users/sign_up.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {
        "first_name": "이름",
        "last_name": "성",
        "email": "Hello@gmail.com",
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        nickname = form.cleaned_data.get("nickname")
        user = authenticate(
            self.request,
            username=email,
            nickname=nickname,
            password=password,
        )
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
