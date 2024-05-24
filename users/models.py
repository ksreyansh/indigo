from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


# User Model Managers
class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email or len(email) <= 0:
            raise ValueError("Email is required!")
        if not password:
            raise ValueError("Password is required!")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, email, password, **extra_fields)


class CustomerManager(models.Manager):
    def create_user(self, username, email, password, **extra_fields):
        if not email or len(email) <= 0:
            raise ValueError("Email is required!")
        if not password:
            raise ValueError("Password is required!")
        email = email.lower()
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=UserAccount.Types.CUSTOMER)
        return queryset


class TellerManager(models.Manager):
    def create_user(self, username, email, password, **extra_fields):
        if not email or len(email) <= 0:
            raise ValueError("Email is required!")
        if not password:
            raise ValueError("Password is required!")
        email = email.lower()
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=UserAccount.Types.TELLER)
        return queryset


# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        TELLER = "TELLER", "Teller"

    user_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=Types.choices, default=Types.CUSTOMER)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
    pin = models.CharField(max_length=6, blank=True)
    country = models.CharField(max_length=50, choices=(('INDIA', 'India'), ('UK', 'United Kingdom'),), null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Special permissions
    is_customer = models.BooleanField(default=False)
    is_teller = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    objects = UserAccountManager()

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        if not self.type or self.type is None:
            self.type = UserAccount.Types.CUSTOMER
        return super().save(*args, **kwargs)


class Customer(UserAccount):
    class Meta:
        proxy = True

    objects = CustomerManager()

    def save(self, *args, **kwargs):
        self.type = UserAccount.Types.CUSTOMER
        self.is_customer = True
        if self.pin and self.type != UserAccount.Types.CUSTOMER:
            self.pin = ''
        return super().save(*args, **kwargs)


class Teller(UserAccount):
    class Meta:
        proxy = True

    objects = TellerManager()

    def save(self, *args, **kwargs):
        self.type = UserAccount.Types.TELLER
        self.is_teller = True
        return super().save(*args, **kwargs)