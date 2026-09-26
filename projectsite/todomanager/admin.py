from django.contrib import admin
from .models import Priority, Category, Task, Note, Subtask

# Register your models here.
admin.site.register(Priority)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Note)
admin.site.register(Subtask)