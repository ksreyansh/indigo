from django.contrib import admin

from .models import UserAccount, Customer, Teller


# Register your models here.
@admin.register(UserAccount)
class UserAccountModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username']


@admin.register(Teller)
class TellerModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username']