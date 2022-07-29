from dataclasses import field
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Password(again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username': 'User Name'}
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'})}


class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomerPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomerPasswordResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))


class CustomerSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="Password",
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="Password (again)",
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
