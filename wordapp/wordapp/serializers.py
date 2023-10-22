# In your Django app's serializers.py

from rest_framework import serializers


class WordDetailsSerializer(serializers.Serializer):
    word = serializers.CharField()
    definition = serializers.CharField()
    usage_sentence = serializers.CharField()
