from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=155, write_only=True)
    confirm_password = serializers.CharField(max_length=155, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password', 'confirm_password')

    def validate(self, attrs):
        passwords = ['qwerty', '123']
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Пароли отличаются"})
        for password in passwords:
            if password in attrs['password']:
                raise serializers.ValidationError({'confirm_password': "Парол легкий"})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password': "меньше 8 символов"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        refresh = RefreshToken.for_user(user)

        return {
            'user': user,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }