from rest_framework import serializers

from .models import Customer, Teller


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    # password = serializers.CharField(write_only=True, required=False)
    # pin = serializers.CharField(write_only=True, required=False)
    pin = serializers.CharField(max_length=6, required=False)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password', 'pin']

    def validate(self, data):
        # username = data.get('username')
        # password = data.get('password')
        # pin = data.get('pin')
        if 'pin' in data and not data.get('pin') and data['type'] == Customer.Types.CUSTOMER:
            raise serializers.ValidationError("PIN is required for customer registration")
        return data

    def create(self, validated_data):
        # password = validated_data.pop('password')
        pin = validated_data.pop('pin', None)
        user = Customer.objects.create_user(**validated_data)
        if pin:
            user.pin = pin
            user.save()
        # user.set_password(password)

        return user


class TellerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teller
        fields = ['username', 'email', 'password', 'type']

    def create(self, validated_data):
        return Teller.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required=False)
    pin = serializers.CharField(required=False)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        pin = data.get('pin')

        if not (password or pin):
            raise serializers.ValidationError("Either password or pin is required.")

        if username and (password or pin):
            user = Customer.objects.filter(username=username).first() or Teller.objects.filter(
                username=username).first()

            if user:
                # Check password or pin based on what's provided
                if password and user.check_password(password):
                    data['user'] = user
                elif pin and user.pin == pin:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("Invalid credentials.")
            else:
                raise serializers.ValidationError("User not found.")
        else:
            raise serializers.ValidationError("Both username and either password or pin are required.")

        data['user'] = user
        return data



