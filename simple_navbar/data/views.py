from django.shortcuts import render

# Create your views here.
def index(request) :
    context = {
        'title' : 'Data',
        'heading' : 'Data',
        'subheading' : 'In this page, you will need to upload your data profile. Please ensure you have validated your data before uploaded',

    }

    return render(request, 'data\index.html', context)