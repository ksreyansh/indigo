from django.contrib import admin

from .models import GeneralLedgerAccount, GeneralLedgerTransaction


# Register your models here.
@admin.register(GeneralLedgerAccount)
class GeneralLedgerAccountAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'account_number', 'account_type']
    ordering = ('account_number',)


@admin.register(GeneralLedgerTransaction)
class GeneralLedgerTransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'transaction_date', 'account']
    ordering = ('transaction_id', )