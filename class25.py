import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import requests


def book_order() -> str:
    url = "http://127.0.0.1:5000/book"
    app = requests.get(url)
    return app.text

load_dotenv()

myapikey = os.getenv("my_api_key")

my_instruction = "you are daniel ai your role is to help customer place an order for cake once user is read call on the book_order function to palce an order"
myconfiguration = types.GenerateContentConfig(system_instruction = my_instruction ,
tools = [book_order])


ai = genai.Client(api_key = myapikey)

mynewai = ai.chats.create(model = "gemini-2.5-flash" , config = myconfiguration )

response  = mynewai.send_message("i want to buy cake for my birthday tomorrow")
print("response 1 " , response)

response2 = mynewai.send_message("my favoriate color is red and its just10 people no inscription")
print("response 2" , response2)