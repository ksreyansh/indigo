from rest_framework import serializers

from .models import TransactionsModel


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionsModel
        exclude_fields = ['description']
        read_only_fields = ['timestamp']