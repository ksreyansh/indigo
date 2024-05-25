from django.db import models

from users.models import UserAccount


# Create your models here.
class BankAccounts(models.Model):
    sid = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    acc_number = models.CharField(max_length=15)
    bal_amount = models.FloatField()

    def save(self, *args, **kwargs):
        self.my_float = round(self.bal_amount, 2)
        super().save(*args, **kwargs)
