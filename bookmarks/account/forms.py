from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    pasword = forms.CharField(widget=forms.PasswordInput)

