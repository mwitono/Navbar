from django.shortcuts import render

# Create your views here.
def index(request) :
    context = {
        'title' : 'CONCAT',
        'heading' : 'CONCATENATE',
        'subheading' : 'CONCATENATE is statiscal modeling projects as the extension of excellent business operational model to explore all possibilities of performance increase and efficiencies, find the right model and implement it in no time.',

    }

    return render(request, 'concatenate\index.html', context)