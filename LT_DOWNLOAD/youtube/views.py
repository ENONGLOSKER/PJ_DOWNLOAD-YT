from django.shortcuts import render
import  os

def index(request):
    context = {
        'judul':'home',
    }
    return render(request, 'index.html',context)
