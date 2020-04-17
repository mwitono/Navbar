from django.shortcuts import render

def index(request) :
    context = {
        'title': 'STT-Analytics',
        'heading': 'CONCATENATE',
        'subheading' : 'EXTEND - EXPLORE - EXPEDITE',
    }
    return render(request, 'index.html', context)