from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    return render(request,'index.html')





# 登录动作

def login_aciton(request):
    if request.met