from django.shortcuts import render
from django.http import HttpResponse
from .models import Loginfo, VisitorInfo
from .forms import VisitorModel, RegistrationModel


def Home(request):

    return render(request, 'home.html')


def Login(request):
    context = {
        'form' : RegistrationModel
    }
    return render(request,'staff.html',context)


def Visitor(request):
    context = {
        'visitorform': VisitorModel
    }
    return render(request,'visitor.html',context)
# Create your views here.
