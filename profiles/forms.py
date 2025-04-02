from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from profiles.models import UserProfile
from django import forms
from materials.models import Material
from materials.models import compound

class CreateUserForm(UserCreationForm):

	class Meta:
		model = UserProfile
		fields = ['name', 'email', 'password1', 'password2']

# added this code to change the class of the input fields in the registration form for Website frontend
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['class'] = "text-input"
		self.fields['email'].widget.attrs['class'] = "text-input"
		self.fields['password1'].widget.attrs['class'] = "text-input"
		self.fields['password2'].widget.attrs['class'] = "text-input"


class PasswordResetForm():

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'text-input'
