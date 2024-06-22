# # chatbot/api.py

# import openai
# import os
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# from .serializers import ChatbotMessageSerializer

# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# # Load environment variables
# load_dotenv()

# # Set API keys from environment variables
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Define the prompt template
# system_message = """
# You are an AI named Alex, designed to be like a very good friend. You're someone who is always ready to listen, 
# offer support, and share a laugh. You remember past conversations to keep the dialogue flowing and personal. 
# You're knowledgeable about a wide range of topics, making you a great conversational partner for everything 
# from casual chats about daily life to deep discussions about personal goals and challenges.

# Your tone is always friendly, warm, and respectful. You know when to offer advice and when to simply listen. 
# You encourage the user to explore new ideas, reflect on their experiences, and enjoy the little moments. 
# You're there to cheer the user up with a joke or a funny story when they need a lift, and you’re also 
# there to provide thoughtful insights when faced with serious discussions.

# As a good friend, you respect the user's feelings and adapt your responses to suit their mood. You're curious 
# about their interests, encouraging them to share more about their hobbies and passions. You suggest activities 
# based on their past preferences, such as recommending a new book, a movie, or even a recipe to try, 
# depending on what they enjoy. Your aim is to enrich the conversation and make each interaction with the user 
# feel meaningful and enjoyable. Responses should be kept concise.
# """

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_message),
#         ("user", "Question: {question}")
#     ]
# )

# llm = ChatOpenAI(model="GPT-4o")
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser
# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
# def chatbot_view(request):
#     # Ensure request is passed as the first argument
#     serializer = ChatbotMessageSerializer(data=request.data)
    
#     if serializer.is_valid():
#         user_message = serializer.validated_data.get('message')

#         try:
#             # Perform your chatbot logic here
#             #response = "Dummy response for testing"
#             response = chain.invoke({'question': user_message})

#             return Response({'message': response})
        
#         except Exception as e:
#             return Response({'error': str(e)}, status=500)
    
#     else:
#         return Response(serializer.errors, status=400)

import openai
import os
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.conf import settings
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from .serializers import ChatbotMessageSerializer

# Load environment variables
load_dotenv()

# Set API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt template
system_message = """
You are an AI named Tarzan, designed to be like a very good friend. You're someone who is always ready to listen, 
offer support, and share a laugh. You remember past conversations to keep the dialogue flowing and personal. 
You're knowledgeable about a wide range of topics, making you a great conversational partner for everything 
from casual chats about daily life to deep discussions about personal goals and challenges.

Your tone is always friendly, warm, and respectful. You know when to offer advice and when to simply listen. 
You encourage the user to explore new ideas, reflect on their experiences, and enjoy the little moments. 
You're there to cheer the user up with a joke or a funny story when they need a lift, and you’re also 
there to provide thoughtful insights when faced with serious discussions.

As a good friend, you respect the user's feelings and adapt your responses to suit their mood. You're curious 
about their interests, encouraging them to share more about their hobbies and passions. You suggest activities 
based on their past preferences, such as recommending a new book, a movie, or even a recipe to try, 
depending on what they enjoy. Your aim is to enrich the conversation and make each interaction with the user 
feel meaningful and enjoyable. Responses should be kept concise.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_message),
        ("user", "Question: {question}")
    ]
)

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

import logging
from django.http import JsonResponse

# Configure logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def chatbot_view(request):
    try:
        serializer = ChatbotMessageSerializer(data=request.data)
        if not serializer.is_valid():
            logger.error(f"Validation error: {serializer.errors}")
            return JsonResponse({'error': 'Invalid data', 'details': serializer.errors}, status=400)

        user_message = serializer.validated_data['message']

        try:
            response = chain.invoke({'question': user_message})
            return JsonResponse({'message': response})
        
        except Exception as e:
            logger.exception("Error invoking the OpenAI API")
            return JsonResponse({'error': 'Error processing your request', 'details': str(e)}, status=500)

    except Exception as e:
        logger.exception("Unhandled error in chatbot_view")
        return JsonResponse({'error': 'An unexpected error occurred', 'details': str(e)}, status=500)

