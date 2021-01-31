from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import operator

def home(request):
    return render(request, 'index.html')

def count(request):
    worddict = {}

    for word in request.GET['fulltext'].split():
        if word in worddict:
            #Increment Count
            worddict[word] += 1
        else:
            #Add word to dictionery
            worddict[word] = 1
    worddict = sorted(worddict.items(), key =operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', { 'fulltext':request.GET['fulltext'],
    'count':len(request.GET['fulltext'].split()), 'dict':worddict })

def aboutUs(request):
    return render(request, 'aboutUs.html')
