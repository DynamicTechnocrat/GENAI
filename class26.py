### genai is stateless
from google import genai
from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv()
saved_memory = [types.Content(role = "user" , parts = [types.Part.from_text(text= "i am happy")]) ,
 types.Content(role = "model" , parts = [types.Part.from_text(text = "Keep that going!")])]

myapikey = os.getenv("my_api_key")
myai = genai.Client(api_key = myapikey)
instruction = "you are jeff your role is to motivate depress fellow make sure the response is very short"
configuration = types.GenerateContentConfig(system_instruction = instruction)
mynewai = myai.chats.create(model = "gemini-3.6-flash" , config = configuration , history = saved_memory)
response = mynewai.send_message("what did we discuss last in our previous chat ")
print(response.text)

### telegram bot >>  genai 