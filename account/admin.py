from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

UserAdmin.fieldsets +=(
    # ('فیلد های شخصی', {"fields": ("phone",)}),
)
admin.site.register(MyUser, UserAdmin)
# admin.site.register(Profile)