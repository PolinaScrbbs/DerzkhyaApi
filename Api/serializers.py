from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User, Ticket

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'role']

        # Дополнительные параметры
        extra_kwargs = {
            'password': {'write_only': True},  #Пароль только для чтения
        }

    #Хеширование пароля
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = super(UserSerializer, self).create(validated_data)
        Token.objects.create(user=user)
        return user
    
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['author', 'title', 'description', 'visiting_time', 'price', 'ticket_count']
