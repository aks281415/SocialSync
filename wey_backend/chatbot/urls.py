from django.urls import path
from . import api

urlpatterns = [
    path('', api.chatbot_view, name='chatbot_view'),
    # Add more URL patterns for other chatbot functionalities as needed
]


