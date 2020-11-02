from django.contrib import admin
from .models import (
    note,
    todo
)
# Register your models here.

admin.site.register(note)
admin.site.register(todo)
