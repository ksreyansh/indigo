from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token

from .models import UserAccount, Customer, Teller


# Register your models here.
@admin.register(UserAccount)
class UserAccountModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username']
    ordering = ('user_id',)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username']
    ordering = ('user_id',)


@admin.register(Teller)
class TellerModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username']
    ordering = ('user_id',)

admin.site.unregister(Group)
