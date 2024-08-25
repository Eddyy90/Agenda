from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from allauth.account.signals import user_logged_in
from allauth.account.views import SignupView, LoginView
from allauth.account.forms import LoginForm


#def logged_in(sender, **kwargs):
#    user = kwargs["user"]
#    request = kwargs["request"]
#    request.session["username"] = user.email
#
#
# Connect django-allauth Signals
#user_logged_in.connect(logged_in)


class SignInView(LoginView):
    template_name = "authentication/login.html"

    def form_invalid(self, form):
        if form.non_field_errors():
            messages.info(self.request, "Credenciais inválidas")
            # messages.info(self.request, form.errors['__all__'][0])
        return super().form_invalid(form)


login = SignInView.as_view()


class RegisterView(SignupView):
    template_name = "authentication/register.html"


register = RegisterView.as_view()


#class ConfirmationEmailView(ConfirmEmailView):
#   template_name = "authentication/register.html"
#confirm_email = ConfirmationEmailView.as_view()

def lockscreen(request):
    if "username" not in request.session:
        return redirect("login")
    else:
        if request.method == "POST":
            userpassword = request.POST.get("userpassword", "default value")
            user = auth.authenticate(password=userpassword)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Credenciais Inválidas")
                return redirect("login")
        else:
            return render(request, "authentication/lockscreen.html")


def logout(request):
    auth.logout(request)
    return render(request, "authentication/logout.html")