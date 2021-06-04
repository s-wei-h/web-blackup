from django.urls import path
from .views import registerFormView, registerHomeView


urlpatterns = [
    path("", registerHomeView, name="registerHome"),
    path("signup/", registerFormView, name="registerForm"),
    path("register/", registerFormView, name="register")
]
