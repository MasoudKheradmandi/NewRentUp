from django.shortcuts import render
from .models import aparteman
# Create your views here.

def listview(request):
    context = {
        'apartemans' : aparteman.objects.all(), 
    }
    return render(request,'posts/listview.html',context)