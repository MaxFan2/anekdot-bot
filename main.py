
import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8095604624:AAGotsTMBoNPykskfLkl78dZgExcHn2opJU"

def load_jokes(filename="jokes.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip().split("===\n")

jokes = load_jokes()

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот-анекдот. Напиши /anekdot и я пришлю смешной анекдот!")

async def anekdot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = random.choice(jokes).strip()
    await update.message.reply_text(joke)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("anekdot", anekdot))
    app.run_polling()

if __name__ == "__main__":
    main()
