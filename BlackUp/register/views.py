from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def registerHomeView(request) :
    return render(request, 'register/index.html')

# def registerFormView(request) :
#     return render(request, 'register/registerForm.html')

def registerFormView(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("register:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="register/registerForm.html", context={"register_form":form})
