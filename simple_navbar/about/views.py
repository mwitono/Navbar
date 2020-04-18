from django.shortcuts import render

# Create your views here.
def index(request) :

    context = {
        'title' : 'About',
        'heading' : 'About',
        'subheading' : 'We are the team of data analyst and application builder. 30 Years total experience in Financial Information Technology and Infrastructure',

    }
    return render(request, 'about\index.html', context)