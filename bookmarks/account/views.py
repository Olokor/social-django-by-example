from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
# Create your views here.
# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             # authenticate checks the credentials entered by the user against the database
#             user = authenticate(request, username=cd['username'], password=cd['password'])

#             if user is not None:
#                 if user.is_active:
#                     # login creates a session for the authenticated user
#                     login(request, user)
#                     return HttpResponse("Authenticated successfully")
#                 else:
#                     return HttpResponse('disabled account')
#             else:
#                 return HttpResponse('invalid username or password')
#     else:
#         form = LoginForm()

#     return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section':'dashboard'}

    )

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object form but avoid saving it

            new_user = user_form.save(commit=False)
            # set the password
            new_user.set_password(
                user_form.cleaned_data['password']
            ) #the set_password method handles password hashing before storing password in the database
            # '''Django doesn’t store clear text passwords; it stores hashed passwords instead. Hashing is the process
            #    of transforming a given key into another value. A hash function is used to generate a fixed-length value
            #    according to a mathematical algorithm. By hashing passwords with secure algorithms, Django ensures
            #    that user passwords stored in the database require massive amounts of computing time to break'''
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)

            return render(request,
'account/register_done.html',
{'new_user': new_user})
        

    else:
        user_form = UserRegistrationForm()
    return render(request,
'account/register.html',
{'user_form': user_form})

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, "Error updating profile!")

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    
    return render(
        request, 'account/edit.html', {
            'user_form':user_form,
            'profile_form':profile_form
        }
    )
    
