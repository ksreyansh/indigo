from django.contrib import admin

from .models import GeneralLedgerAccount


# Register your models here.
@admin.register(GeneralLedgerAccount)
class GeneralLedgerAccountAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'account_number', 'account_type']
    ordering = ('account_number',)