from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def url1(request):
    url1 = '<a href="https://www.w3schools.com/html/html_links.asp">w3 schools</a>'
    return HttpResponse(url1)

#def learn_python(request):
 #   return HttpResponse('<h1>Hello Python</h1>')
def learn_var(request):
    a='<h1> Hello Variable</h1>'
    return HttpResponse(a)

#def learn_math(request):
 #   a=10+10
  #  return HttpResponse(a)
