from django import forms

class LogIn(forms.Form):
    handle = forms.CharField(label = "Handle ",max_length = 30)
    password = forms.CharField(label = "Password ", widget = forms.PasswordInput())