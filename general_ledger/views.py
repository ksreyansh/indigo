from rest_framework import viewsets

from .models import GeneralLedgerAccount, GeneralLedgerTransaction
from .serializers import GLAccountSerializer, GLTransactionSerializer


# Create your views here.
class GLAccountViewSet(viewsets.ModelViewSet):
    queryset = GeneralLedgerAccount.objects.all()
    serializer_class = GLAccountSerializer


class GLTransactionViewSet(viewsets.ModelViewSet):
    queryset = GeneralLedgerTransaction.objects.all()
    serializer_class = GLTransactionSerializer
