from django.contrib import admin
from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('listview/',views.listview,name='listview'),
    path('det/<id>/',views.detailview,name='detailview'),
]
