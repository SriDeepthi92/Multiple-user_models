from django.shortcuts import render
from profiles.forms import CreateUserForm
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from profiles.forms import CreateUserForm
from django.http import JsonResponse

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

######
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages #import messages
from django.contrib.auth.views import PasswordResetCompleteView


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "registrations/password_reset_complete.html"
	
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = UserProfile.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registrations/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'something.com',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'EMAIL_HOST_USER', [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')

					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("home")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registrations/password_reset.html", context={"password_reset_form":password_reset_form})


def SignupPage(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('name')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')


		context = {'form':form}
		return render(request, 'registrations/signup.html', context)

def loginPage(request):
		if request.method == 'POST':
			name = request.POST.get('name')
			password =request.POST.get('password')

			user = authenticate(request, username=name, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'registrations/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):
    return render(request, 'index.html')