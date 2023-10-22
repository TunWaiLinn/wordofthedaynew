from django.shortcuts import render

# Create your views here.
# In your Django app's views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scraper import get_word_details  # Import your get_word_details function
from .serializers import WordDetailsSerializer


@api_view(['GET'])
def word_details(request):
    word, definition, usage_sentence = get_word_details()
    data = {
        'word': word,
        'definition': definition,
        'usage_sentence': usage_sentence,
    }
    serializer = WordDetailsSerializer(data)
    return Response(serializer.data)
