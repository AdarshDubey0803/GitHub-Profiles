from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	first_name = forms.CharField(max_length = 30,required = True)
	last_name = forms.CharField(max_length = 30,required = False)
	class Meta:
		model = User
		fields = ("username", "password1", "password2", "first_name", "last_name")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user
