from django.contrib import admin

# Register your models here.
from .models import Kurs,Student, Prepod

admin.site.register(Kurs)
admin.site.register(Student)
admin.site.register(Prepod)
