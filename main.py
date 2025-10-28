from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 🧠 Telegram AI Bot by Reyansh
# 24x7 Free Open-source AI Auto-Reply Bot 🚀

import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

OPENAI_API_KEY = "sk-...-XEA"
TELEGRAM_BOT_TOKEN = "8442464558:AAFqTZNiSPLx1R4iBelpWB_NRoJ4XQJrM-8"

openai.api_key = OPENAI_API_KEY

# 👋 Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey 👋, I'm your 24x7 AI bot powered by OpenAI. Ask me anything!")

# 💬 Chat with AI
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}]
        )

        reply = response.choices[0].message.content
        await update.message.reply_text(reply)

    except Exception as e:
        await update.message.reply_text("⚠️ Error: " + str(e))

# 🚀 Main function
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("🤖 Bot is running 24×7...")
    keep_alive()
    if __name__ == "__main__":
    from threading import Thread
    Thread(target=app.run_polling).start()
    from flask import Flask
    alive = Flask(__name__)

    @alive.route('/')
    def home():
        return "Bot is Alive"

    alive.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    main()
