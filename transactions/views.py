from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import TransactionsModel
from .serializers import TransactionSerializer
from general_ledger.models import GeneralLedgerAccount, GeneralLedgerTransaction


# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = TransactionsModel.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.save()

        # Update Account balance
        account = transaction.account
        match transaction.transaction_type:
            case "DEPOSIT":
                account.bal_amount += transaction.amount
            case "WITHDRAWAL":
                account.bal_amount -= transaction.amount
            case "TRANSFER":
                match transaction.accounting_type:
                    case "CR":
                        account.bal_amount += transaction.amount
                    case "DR":
                        account.bal_amount -= transaction.amount
        account.save()

        # General Ledger Entries
        if transaction.transaction_type in ['deposit', 'withdrawal']:
            cash_account = GeneralLedgerAccount.objects.get(account_number='1000')
            user_account = GeneralLedgerAccount.objects.get(account_number=account.account_number)

            if transaction.transaction_type == 'deposit':
                GeneralLedgerTransaction.objects.create(
                    account=GeneralLedgerAccount.objects.get(account_number="1000"),
                    transaction_date=transaction.timestamp,
                    description=transaction.description,
                    debit=0.00,
                    credit=transaction.amount
                )
                GeneralLedgerTransaction.objects.create(
                    account=GeneralLedgerAccount.objects.get(account_number="2020"),
                    transaction_date=transaction.timestamp,
                    description=transaction.description,
                    debit=0.00,
                    credit=transaction.amount
                )
            elif transaction.transaction_type == 'withdrawal':
                GeneralLedgerTransaction.objects.create(
                    account=GeneralLedgerAccount.objects.get(account_number="1000"),
                    transaction_date=transaction.timestamp,
                    description=transaction.description,
                    debit=transaction.amount,
                    credit=0.00
                )
                GeneralLedgerTransaction.objects.create(
                    account=GeneralLedgerAccount.objects.get(account_number="2020"),
                    transaction_date=transaction.timestamp,
                    description=transaction.description,
                    debit=transaction.amount,
                    credit=0.00
                )
