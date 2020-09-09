from django.contrib import admin

# Register your models here.
from todo.models import Todo, Category

admin.site.register(Todo)
admin.site.register(Category)

