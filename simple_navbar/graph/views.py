from django.shortcuts import render

# Create your views here.
def index(request) :
    context = {
        'title' : 'Graph',
        'heading' : 'Graph',
        'subheading' : 'Show your charts here',

    }

    return render(request, 'graph\index.html', context)