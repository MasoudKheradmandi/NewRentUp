from django.shortcuts import render ,redirect
from .forms import KhabarnameForm
from .models import Khabarname
from django.http import HttpResponse
# Create your views here.

def khabarnameView(request):
    if request.method == "POST":
        form = KhabarnameForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            Khabarname.objects.create(
                email = email
            )
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse("Form Is not valid")
    else:
        form = KhabarnameForm()
    context ={
        'form':form
    }

    return render(request,'home.html',context)            