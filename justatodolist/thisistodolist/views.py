from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages



def home(request):
	if request.method == 'POST':

		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all()
			messages.success(request, ('新任务添加成功'))

			return render(request, 'home.html', {'all_items': all_items})
	else:
		all_items = List.objects.all()

		messages.warning(request, ('任何新的想法？'))

		return render(request, 'home.html', {'all_items': all_items}) 



def delete(request, list_id):
	item = List.objects.get(pk=list_id) 
	item.delete()
	messages.success(request, ('删除成功！'))
	return redirect('home')


# 已经完成的任务，标记为cross_off 
def done(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')


# 已经完成的某个任务，如果后悔了，想恢复，用这个可以恢复
def going(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')


def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ('修改成功！'))
			return redirect('home')

	else:
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item': item})