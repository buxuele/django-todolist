from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def showAll(request):
    allItems = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': allItems})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect("/todo/")       # return upper level url


def deleteTodo(request, myid):
    item_deleting = TodoItem.objects.get(id=myid)
    item_deleting.delete()
    return HttpResponseRedirect("/todo/")

