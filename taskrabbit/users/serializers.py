from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        
    