from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # authenticate checks the credentials entered by the user against the database
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    # login creates a session for the authenticated user
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse('disabled account')
            else:
                return HttpResponse('invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})
