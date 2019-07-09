#!/usr/bin/python3
# Time: 2019/07/09 8:51 PM
# About:


"""
1. 多注意拼写错误！！！　这个很严重！
２．　url  path, 前面的斜杠不重要，　后面一个斜杠一定要写上．．．


"""

from django.urls import path
from .views import showAll, addTodo, deleteTodo

urlpatterns = [
    path('', showAll, name="show_all_items"),
    path('addTodo/', addTodo, name="add_new_items"),
    path('deleteTodo/<int:myid>/', deleteTodo, name="delete_items"),
]



