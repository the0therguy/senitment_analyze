from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .sentiment import *


# Create your views here.
@api_view(('POST',))
def analyze(request):
    analyze = request.data
    data = sentiment(analyze.get('text'))
    sentiment_value = ''
    score = float('-inf')
    for d in data:
        if d.get('score') >= score:
            sentiment_value = d.get('label')
            score = d.get('score')
    return Response({'sentiment': sentiment_value.lower()})
