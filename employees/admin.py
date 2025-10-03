from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'department', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

