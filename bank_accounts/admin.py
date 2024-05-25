from django.contrib import admin

from .models import BankAccounts


# Register your models here.
@admin.register(BankAccounts)
class BankAccountsModelAdmin(admin.ModelAdmin):
    list_display = ['acc_number', 'acc_type', 'user_id']
    ordering = ('acc_number', )