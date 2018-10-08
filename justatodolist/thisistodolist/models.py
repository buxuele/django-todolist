from django.db import models


'''
1. 一旦新建了 数据库 models, 需要重新 进行数据库迁移
2. 新建一个 forms.py文件， 一个数据库model 对应一个 Form(class)
3. 回到 views, 开始使用这些数据


'''

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.item + ' | ' + str(self.completed)