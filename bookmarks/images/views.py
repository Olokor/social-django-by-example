from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateFrom
# from django.contrib.auth.models import User
# Create your views here.
@login_required
def image_create(request):
    print("the bginige of this view")
    if request.method == 'POST':
        form = ImageCreateFrom(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print('hii')
            new_image = form.save(commit=False)
        
            #assign current user to this image before saving
            new_image.user = request.user
            
            new_image.save()
        
            messages.success(request, 'Image added successfully', )
            return redirect(new_image.get_absolute_ur())
    else:
        form = ImageCreateFrom(data=request.GET)
    
    return render(
        request, 'images/image/create.html',
        {
            'form':form,
            'section':'images'
        }
    )