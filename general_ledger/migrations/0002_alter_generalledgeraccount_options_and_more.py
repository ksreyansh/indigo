# Generated by Django 5.0.6 on 2024-05-25 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general_ledger", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="generalledgeraccount",
            options={
                "verbose_name": "General Ledger Account",
                "verbose_name_plural": "General Ledger Accounts",
            },
        ),
        migrations.CreateModel(
            name="GeneralLedgerTransaction",
            fields=[
                ("transaction_id", models.AutoField(primary_key=True, serialize=False)),
                ("transaction_date", models.DateField()),
                ("description", models.CharField(blank=True, max_length=255)),
                (
                    "debit",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
                ),
                (
                    "credit",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="general_ledger.generalledgeraccount",
                    ),
                ),
            ],
            options={
                "verbose_name": "General Ledger Transaction",
                "verbose_name_plural": "General Ledger Transactions",
            },
        ),
    ]
