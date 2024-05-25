from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GLAccountViewSet, GLTransactionViewSet

router = DefaultRouter()
router.register(r'accounts', GLAccountViewSet)
router.register(r'transactions', GLTransactionViewSet)

urlpatterns = [
    path('', include(router.urls))
]