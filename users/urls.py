from django.urls import path

from .views import CustomerRegistrationView, TellerRegistrationView, UserLoginView

urlpatterns = [
    path('customer/register/', CustomerRegistrationView.as_view(), name="cust-reg"),
    path('teller/register/', TellerRegistrationView.as_view(), name="tell-reg"),
    path('login/', UserLoginView.as_view(), name="login"),
]