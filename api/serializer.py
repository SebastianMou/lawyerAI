from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ContractProject, AIHighlightChat

class AIHighlightChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIHighlightChat
        fields = '__all__'

class ContractProjectSerializer(serializers.ModelSerializer):
    ai_chats = AIHighlightChatSerializer(many=True, read_only=True)  # Add this line to include related AI chats

    class Meta:
        model = ContractProject
        fields = '__all__'
