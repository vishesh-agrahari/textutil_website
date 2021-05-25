from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext =request.GET.get('text','defualt')
    removepunc =request.GET.get('removepunc','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    if removepunc =="on":
        analyzed =''
        punctuations ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
           if char not in punctuations:
                   analyzed =analyzed + char
        params = {'purpose': '', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if (newlineremover == "on"):
         analyzed =''
         for char in djtext:
             if char !='\n' and char !='\r':
                 analyzed = analyzed + char
             else:
                 analyzed = analyzed + " "
         params = {'purpose': '', 'analyzed_text': analyzed}
         djtext = analyzed
         # return render(request, 'analyze.html', params)
    if (fullcaps == "on"):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': '', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if(removepunc !='on' and newlineremover !='on' and fullcaps !='on'):
        return HttpResponse('Error!! please select at least on one operation')
    return render(request, 'analyze.html', params)


