import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN was not found in .env")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋")


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    await update.message.reply_text(f"You said: {message}")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()