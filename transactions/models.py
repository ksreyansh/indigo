from django.db import models

from bank_accounts.models import BankAccounts


# Create your models here.
class TransactionsModel(models.Model):
    TRANSACTION_TYPES = (
        ("DEPOSIT", "Deposit"),
        ("WITHDRAWAL", "Withdrawal"),
        ("TRANSFER", "Transfer")
    )

    ACCOUNTING_TYPES = (
        ("DR", "Debit"),
        ("CR", "Credit")
    )

    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(BankAccounts, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    accounting_type = models.CharField(max_length=15, choices=ACCOUNTING_TYPES, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.transaction_id} ({self.accounting_types}"


class TransferTransactions(models.Model):
    ACCOUNTING_TYPES = (
        ("DR", "Debit"),
        ("CR", "Credit")
    )

    transaction_id = models.AutoField(primary_key=True)
    source_account = models.ForeignKey(BankAccounts, on_delete=models.CASCADE, related_name="source_acc")
    destination_account = models.ForeignKey(BankAccounts, on_delete=models.CASCADE, related_name="dest_acc")
    accounting_types = models.CharField(max_length=5, choices=ACCOUNTING_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Update source and destination account balances
        if self.accounting_type == 'CR':
            self.source_account.bal_amount -= self.amount
            self.destination_account.bal_amount += self.amount
        elif self.accounting_type == 'DR':
            self.source_account.bal_amount += self.amount
            self.destination_account.bal_amount -= self.amount

        self.source_account.save()
        self.destination_account.save()


