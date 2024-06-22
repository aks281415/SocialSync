from django.shortcuts import render

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Set API keys from environment variables
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# ## Langmith tracking
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# ## Enhanced Prompt Template
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
# feel meaningful and enjoyable. Responses should be kept concised.
# """

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_message),
#         ("user", "Question: {question}")
#     ]
# )

# ## OpenAI Language Model
# llm = ChatOpenAI(model="gpt-3.5-turbo")
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser

# def run_chat():
#     print("Hello! I'm Corey, your AI friend. Feel free to ask me anything or just share what's on your mind. I'm here to listen and help!")

#     while True:
#         input_text = input("You: ")
#         # Check for exit or goodbye keywords
#         if input_text.lower() in ['exit', 'bye']:
#             print("It was great chatting with you! Have a wonderful day and talk to you soon!")
#             break
#         # Generate and print the response
#         response = chain.invoke({'question': input_text})
#         print(f"Alex: {response}")

# # Run the chat function
# if __name__ == "__main__":
#     run_chat()

