from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import *

# Create your views here.
def Home(request):
    return render(request,'base/index.html')

def Contact(request):
    return render(request,"other/add.html")