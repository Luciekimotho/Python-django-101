from django.db import models

# Create your models here.

class Student(models.Model):
	full_name = models.CharField(max_length = 200)
	age = models.IntegerField()
	email = models.EmailField()
	interest = models.TextField()
	registered_date = models.DateField(auto_now = False, auto_now_add = True)
	last_update = models.DateField(auto_now = True, auto_now_add = False)
	
	def __str__(self):
	   return self.full_name

class Classrooms(models.Model):
	name = models.CharField(max_length = 200)
	floor = models.CharField(max_length = 200)
	has_podium = models.BooleanField()
	commissioned_date = models.DateField(auto_now = False, auto_now_add = True)
	created_at = models.DateField(auto_now = False, auto_now_add = True)
	updated_at = models.DateField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.name

		
