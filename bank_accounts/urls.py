from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BankAccountsViewSet

router = DefaultRouter()
router.register(r'accounts', BankAccountsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
