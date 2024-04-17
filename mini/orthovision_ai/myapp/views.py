from django.shortcuts import render
from django.http import HttpResponse
def login(request):
    context={}
    return render(request,'myapp/Login.html',context)
def signup(request):
    context={}
    return render(request,'myapp/Signup.html',context)
def upload(request):
    context={}
    return render(request,'myapp/Upload.html',context)