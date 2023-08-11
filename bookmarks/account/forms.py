from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    pasword = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords does not match")
        return cd['password2']
    
    def clean_email(self):
        data = self.changed_data['email']
        if User.objects.get(email=data).exists():
            raise forms.ValidationError("Email already exist!")
        return data
    


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.changed_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)

        if qs.exists():
            raise forms.ValidationError("email already exist")
        return data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']

