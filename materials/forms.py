from django.forms import ModelForm
from django import forms
from materials.models import Material
from materials.models import compound
from django.utils.translation import gettext_lazy as _
from django.forms import Form, HiddenInput, CharField, ChoiceField, ModelForm



class compoundForm(ModelForm):
	class Meta:
		model = compound
		fields = '__all__'