from rest_framework import serializers

from .models import BankAccounts


class BankAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccounts
        fields = ['user',
                  'acc_type',
                  'bal_amount',
                  'city',
                  'state',
                  'country',
                  'status']
        read_only_fields = ['acc_number']
