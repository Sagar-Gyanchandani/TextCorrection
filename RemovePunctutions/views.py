from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # // Get text
    djtext = request.POST.get('text', 'default') 


    djpunc = request.POST.get('punc', 'off')
    caps = request.POST.get('caps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    
    analyze = djtext
    params = {}
    

    if djpunc == 'on':
        analyze = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        params = {'analyzed_text': analyze, 'purpose': 'Remove Punctuations'} 

        djtext = analyze

    if (caps == "on"):
        
        analyze = ''
        for char in djtext:
            analyze = analyze + char.upper() 
        djtext = analyze
        params = {'analyzed_text': analyze, 'purpose': 'Capitalize all words'} 
        
    if (spaceremover == "on"):
        analyze = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyze = analyze + char 

        params = {'analyzed_text': analyze, 'purpose': 'Space remover'}    

        djtext = analyze
    
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            
        
        params = {'analyzed_text': analyze, 'purpose': 'Remove NewLine'} 


    if(djpunc != "on" and caps!="on" and newlineremover!="on" and spaceremover!="on"):
        return HttpResponse("please select any operation and try again")
        

       
    return render(request, 'analyze.html', params) 
    