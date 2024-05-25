from django.db import models
from \
    django.utils import timezone
import random
from users.models import UserAccount
from master_data.models import Country, State, City, AccountType


def generate_unique_account_number(user_id, state_code, country_code):
    current_time = int(timezone.now().timestamp() * 1000)
    random_number = random.randint(0, 99)

    # Ensuring the timestamp and random number fit within the desired length
    current_time_str = str(current_time)[:3]  # Adjusted to ensure proper length
    random_number_str = str(random_number).zfill(3)

    # Retrieve the codes from the provided objects
    country_code = country_code[:2]
    state_code = state_code[:2]

    if len(str(user_id)) == 1:
        user_id = f"0000{user_id}"
    elif len(str(user_id)) == 2:
        user_id = f"000{user_id}"
    elif len(str(user_id)) == 3:
        user_id = f"00{user_id}"
    elif len(str(user_id)) == 4:
        user_id = f"0{user_id}"
    else:
        pass

    # Construct the account number
    account_number = f"{country_code}{state_code}{user_id}{current_time_str}{random_number_str}"
    account_number = account_number[:15]  # Ensure the final length is within 15 characters

    return account_number


# Create your models here.
class BankAccounts(models.Model):
    STATUS_CHOICES = (("INACTIVE", "Inactive"),
                      ("ACTIVE", "Active"),
                      ("DORMANT", "Dormant"),
                      ("CLOSED", "Closed"),)

    sid = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    acc_number = models.CharField(max_length=15, blank=True)
    acc_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True)
    bal_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=5, default="INR")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")

    def save(self, *args, **kwargs):
        if not self.acc_number:  # Generate account number only if it's not already set
            self.acc_number = generate_unique_account_number(self.user.user_id, self.state.state_code, self.country.country_code)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.acc_number

    class Meta:
        verbose_name = "Bank Account"
        verbose_name_plural = "Bank Accounts"
