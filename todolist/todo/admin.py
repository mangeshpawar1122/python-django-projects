from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('title','description','complated')
  list_filter = ('complated','created_at')
  search_fields = ('title','description')
  ordering = ('-created_at',)