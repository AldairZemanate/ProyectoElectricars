from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('user_name','user_lastname','is_active')
    list_filter=('is_active','user_type',)