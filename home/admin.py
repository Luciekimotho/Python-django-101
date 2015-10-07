from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Classrooms
from .forms import StudentForm

class StudentAdmin(admin.ModelAdmin):
	form = StudentForm

admin.site.register(Student, StudentAdmin)
admin.site.register(Classrooms)