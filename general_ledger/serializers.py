from rest_framework import serializers

from .models import GeneralLedgerAccount, GeneralLedgerTransaction


class GLAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralLedgerAccount
        fields = "__all__"


class GLTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralLedgerTransaction
        exclude = ('description', )