from flask import Flask, request
import telegram
import openai
import os

# 🔹 Set your API keys
TELEGRAM_BOT_TOKEN = "8442464558:AAFqTZNiSPLx1R4iBelpWB_NRoJ4XQJrM-8"
OPENAI_API_KEY = "sk-...-XEA"

# 🔹 Initialize
app = Flask(__name__)
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

@app.route('/')
def home():
    return "🤖 Bot is Alive!"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    # ✅ Handle message
    if update.message and update.message.text:
        user_text = update.message.text

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_text}]
            )
            reply = response.choices[0].message.content
            import asyncio
asyncio.run(bot.send_message(chat_id=update.message.chat_id, text=reply))
        except Exception as e:
await bot.send_message(chat_id=update.message.chat_id, text=f"⚠️ Error: {e}")

    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host="0.0.0.0", port=port)
