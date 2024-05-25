from django.db import models


# Create your models here.
class GeneralLedgerAccount(models.Model):
    CHOICES = (("ASSET", "Asset"),
               ("LIABILITY", "Liability"),
               ("EQUITY", "Equity"),
               ("REVENUE", "Revenue"),
               ("EXPENSE", "Expense"))

    account_number = models.CharField(max_length=10, primary_key=True)
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return f"{self.account_number} - {self.account_name}"

    class Meta:
        verbose_name = "General Ledger Account"
        verbose_name_plural = "General Ledger Accounts"


class GeneralLedgerTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(GeneralLedgerAccount, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    debit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"TX {self.transaction_id} on {self.transaction_date}"

    class Meta:
        verbose_name = "General Ledger Transaction"
        verbose_name_plural = "General Ledger Transactions"
