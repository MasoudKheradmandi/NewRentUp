from django.shortcuts import render
from .models import commentHome
from posts.models import aparteman
# Create your views here.
def home(request):
    context = {
    "CommentHome":commentHome.objects.all(),
    "apartemans":aparteman.objects.filter(active=True)
    }
    return render(request,'home.html',context)

