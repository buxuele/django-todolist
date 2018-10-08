from django.contrib import admin
from django.urls import path
from . import views

''''
1. 这个文件是 项目一开始的时候就创建的，注意一些包的引入
2. view.py中，每一个函数都必须对应 一个 path 


'''


urlpatterns = [
	path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('done/<list_id>', views.done, name='done'),
    path('going/<list_id>', views.going, name='going'),
    path('edit/<list_id>', views.edit, name='edit'),
]