from django.shortcuts import render,get_object_or_404
from .models import aparteman,aparteman_images

# Create your views here.

def listview(request):
    context = {
        'apartemans' : aparteman.objects.filter(active=True), 
    }
    return render(request,'posts/listview.html',context)


def detailview(request,id):
    x = get_object_or_404(aparteman,id=id)
    context = {
        'x':x,
        'aparteman_images':aparteman_images.objects.filter(id=id)
    }
    return render(request,'posts/detail.html',context)