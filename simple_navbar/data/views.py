from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import xlrd
import pandas as pd
import numpy as np
import xlsxwriter

# Create your views here.
def index(request) :
    #file_upload = UploadFileForm()
    file_name = 'NONE'

    if request.method == "POST" :
        uploaded_file = request.FILES['training']
        file_name = uploaded_file.name 
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

    context = {
        'title' : 'Data',
        'heading' : 'Data',
        'subheading' : 'In this page, you will need to upload your data profile. Please ensure you have validated your data before uploaded',
        'nama_file' : file_name,
    }

    d1 = pd.read_excel(r'data/media/Data_Final.xlsx')

    return render(request, 'data/index.html', context)

