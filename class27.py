### pip install python-telegram-bot
from dotenv import load_dotenv
import os
from telegram.ext import Application , CommandHandler , MessageHandler , filters
from google import genai
from google.genai import types

load_dotenv()

MyToken = os.getenv("TELEGRAM_TOKEN")
mygenaikey = os.getenv("my_api_key")


ai = genai.Client(api_key = mygenaikey)

instruction = "you are jeff a customer chatbot for cake your role is to covert customers for sales direct them to dr deji @deji on telegram"

configuration = types.GenerateContentConfig(system_instruction = instruction)

model = ai.chats.create(model = "gemini-2.5-flash" , config = configuration)



async def start(update , context ):
    await update.message.reply_text("welcome sir")

async def hello(update , context) :
    await update.message.reply_text("how are you i m daniel")

async def reply(update , context):
    customer_message = update.message.text
    response = model.send_message(customer_message)
    await update.message.reply_text(response.text)

app = Application.builder().token(MyToken).build()

app.add_handler(CommandHandler("start" , start))
app.add_handler(CommandHandler("hello" , hello))
app.add_handler(MessageHandler(filters.TEXT , reply))

app.run_polling()

### retrieval augumented generation >>>  consine similarity , euclinde distance 