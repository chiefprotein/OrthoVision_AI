from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from .forms import XrayImgForm
from .models import XrayImages
def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload')
        else:
            messages.error(request, ("Invalid username or password"))
            storage = messages.get_messages(request)
            storage.used = True
    return render(request, 'myapp/login.html')
def signup(request):
    context={}
    return render(request,'myapp/Signup.html',context)
def upload(request):
 
    if request.method == 'POST':
        form = XrayImgForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = XrayImgForm()
    context = {'form': form}
    return render(request, 'myapp/Upload.html', context)
 
 
def success(request):
    last_uploaded_image = XrayImages.objects.last()
    return render(request, 'myapp/success.html', {'success': last_uploaded_image})