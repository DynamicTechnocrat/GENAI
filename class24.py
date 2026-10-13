import os
from dotenv import load_dotenv
from google import genai
from flask import Flask,request
### load api key
load_dotenv()


mykey = os.getenv("my_api_key")
client = genai.Client(api_key = mykey)
chat = client.chats.create(model = "gemini-2.5-flash")

app = Flask(__name__)

@app.route("/watai" , methods = ["POST"])
def generalai():
    prompt = request.json.get("message")
    names = request.json.get("name")
    whole_message = prompt + "my name is " + names
    response = chat.send_message(whole_message)
    return response.text

if __name__ == "__main__":
    app.run(debug = True)