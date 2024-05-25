from rest_framework import viewsets

from .models import BankAccounts
from .serializers import BankAccountsSerializer


# Create your views here.
class BankAccountsViewSet(viewsets.ModelViewSet):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountsSerializer
