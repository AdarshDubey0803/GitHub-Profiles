from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


userList = User.objects.values()
datalist = []

def homepage(request):
	return render(request=request, template_name='GitHub_Profiles/home.html')
	
def dash_home(request):
	return render(request = request, template_name='GitHub_Profiles/dash_home.html')
	
def explore(request):
	return render(request=request, template_name='GitHub_Profiles/explore.html', context = {"data":datalist})
	
def logout_request(request):
	logout(request)
	return redirect("login")
	
def profiles(request, username):
	return render(request = request, template_name = 'GitHub_Profiles/profile.html', context = {'dataset':datalist})

import requests
	
def dash_cred(username):
	response = requests.get('https://api.github.com/users/'+str(username))
	if response.status_code == 200 :
		json_response = response.json()
		my_dict = {"UserName":json_response['login'], "Name":json_response['name'], "Followers":json_response['followers'], "LastUpdate":json_response['updated_at']}
		return my_dict
	elif response.status_code == 404 :
		print("No Such GitHub Username Found")
		
for i in userList[1:] :
	if i["id"] != 1 :
		datalist.append(dash_cred(i["username"]))

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
			global userList
			userList = User.objects.values()
			global datalist
			datalist.append(dash_cred(user.username))
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="GitHub_Profiles/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="GitHub_Profiles/login.html", context={"login_form":form})


