from django.contrib import admin

from .models import Country, State, City, AccountType


# Register your models here.
@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ['country_code', 'country_name']
    ordering = ('country_code',)


@admin.register(State)
class StateModelAdmin(admin.ModelAdmin):
    list_display = ['state_code', 'state_name', 'country_code']
    ordering = ('state_code',)


@admin.register(City)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ['city_code', 'city_name', 'state_code']
    ordering = ('city_code',)


@admin.register(AccountType)
class AccountTpeAdmin(admin.ModelAdmin):
    list_display = ['type_id', 'type_name']
    ordering = ('type_id', )