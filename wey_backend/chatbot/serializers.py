# chatbot/serializers.py

from rest_framework import serializers

class ChatbotMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
