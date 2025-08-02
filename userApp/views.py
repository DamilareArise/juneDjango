from django.shortcuts import render
from django.views import generic
from .forms import SignupForm
from django.urls import reverse_lazy

# Create your views here.
class SignupView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'