from django.contrib import admin
from django.urls import path
from . import views

app_name='youtubeapp'

urlpatterns = [
    path('download/',views.downloader, name='download'),
    path('done/<resolution>/',views.done, name='done'),
]
