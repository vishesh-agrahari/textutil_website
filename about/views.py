from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_math(request):
   a=10+10
   return HttpResponse(a)
def temp(request):
   return render(request,'registration.html')