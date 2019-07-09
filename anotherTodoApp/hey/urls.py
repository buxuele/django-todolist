#!/usr/bin/python3
# Time: 2019/07/09 8:41 PM
# About: 


from django.urls import path
from .views import myView

urlpatterns = [
    path('', myView, name="firstView"),
]































