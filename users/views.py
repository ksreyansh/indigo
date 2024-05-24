from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.authtoken.models import Token

from .models import UserAccount, Customer, Teller
from .serializers import CustomerRegistrationSerializer, TellerRegistrationSerializer, LoginSerializer


# Create your views here.
class CustomerRegistrationView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data
        user_instance = Customer.objects.get(username=user['username'])
        # token = Token.objects.get_or_create(user=user_instance)
        return Response({'user': user}, status=status.HTTP_201_CREATED)


class TellerRegistrationView(generics.CreateAPIView):
    queryset = Teller.objects.all()
    serializer_class = TellerRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data
        user_instance = Teller.objects.get(username=user['username'])
        # token = Token.objects.get_or_create(user=user_instance)
        return Response({'user': user}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
