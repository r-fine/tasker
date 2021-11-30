from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


from accounts.forms import RegisterStaffForm
from accounts.decorators import unauthenticated_user


@unauthenticated_user()
class RegisterStaffView(SuccessMessageMixin, CreateView):
    login_url = 'auth/logout'
    template_name = 'staff/register-staff.html'
    form_class = RegisterStaffForm
    success_url = reverse_lazy('account_login')
    success_message = "Profile Created"