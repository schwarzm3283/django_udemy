from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):

    piglatin = request.GET['origtext']

    translation = ''
    for word in piglatin.split():
        word = word.lower()
        if word[0] in ['a','e','i','o','u']:
            #vowel
            translation += word
            translation += ' vowel '
        else:
            #consanant
            translation += word
            translation += ' consanant '

    return HttpResponse("you're on translate page " + translation)
