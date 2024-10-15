from django.http import HttpResponse
from django.shortcuts import render
from setuptools.command.bdist_egg import analyze_egg


def index(request):
    return render(request, 'index2.html')
def analyze(request):
    djtext =request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcap=request.POST.get('fullcap','off')
    removenewline = request.POST.get('removenewline', 'off')
    charcount = request.POST.get('charcount', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    removenumbers = request.POST.get('removenumbers', 'off')


    print(removepunc)
    print(djtext)
    if removepunc=='on':

        puntuations ='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        #analyzed=djtext
        for char in djtext:
            if char not in puntuations:
                analyzed += char

        params = {'purpose': ' Removed puntutions', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcap=='on'):
        analyzed = ''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': ' UPPER CASE', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze2.html', params)


    if (removenewline == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '/n':
                analyzed = analyzed + char
        params = {'purpose': ' New line remove', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze2.html', params)

    if (charcount == 'on'):
        print("total charcount :")
        analyzed = len(djtext)  # This counts the charcount in djtext
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)

    if (lowercase == 'on'):
        analyzed = djtext.lower()  # Convert text to lowercase
        params = {'purpose': ' Converted to Lowercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if (removenumbers == 'on'):
        analyzed = ''.join(char for char in djtext if not char.isdigit())
        params = {'purpose': ' Removed Numbers', 'analyzed_text': analyzed}



        djtext = analyzed


    if(removenewline != 'on' and lowercase != 'on' and charcount != 'on' and removenumbers != 'on' and fullcap != 'on' and removepunc !='on'):
        return HttpResponse("please select any option")

    return render(request ,'analyze2.html',params)