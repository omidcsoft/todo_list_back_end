from .models import ToDo
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"

class TokenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"