from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from app.forms import CustomerRegistrationForm


def home(request):
    return render(request, 'app/home.html')


def profile(request):
    return render(request, 'app/profile.html')


def change_password(request):
    return render(request, 'app/changepassword.html')


def login(request):
    return render(request, 'app/login.html')


class CustomerRegistration(View):
    def get(self, request):
        fm = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': fm})

    def post(self, request):
        fm = CustomerRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
