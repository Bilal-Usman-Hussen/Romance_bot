import os
import random
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, MessageHandler, filters

TOKEN = os.environ.get("8584367283:AAEV4zYnPKVjkHspVLEgBRUY8743Bnmzrn0")       # Your Bot token from BotFather
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # Render app URL

bot = Bot(token=TOKEN)
app = Flask(__name__)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)

# Simple in-memory user storage
user_names = {}  # chat_id -> first_name

# Romantic message components
openings = ["Hey {name},", "My love {name},", "Sweetheart {name},", "Darling {name},", "Angel {name},",
            "Sunshine {name},", "My heart {name},", "Cutie {name},", "My queen {name},", "Precious {name},"]
middles = [
    "every time I think of you, my heart skips a beat.",
    "you light up my world like the sunrise.",
    "I feel lucky just knowing you exist.",
    "you are the reason my days feel magical.",
    "my heart feels safe with you.",
    "you make ordinary moments extraordinary.",
    "thinking about you makes me smile uncontrollably.",
    "your presence makes everything better.",
    "you are my favorite thought.",
    "you make life feel like a beautiful dream."
]
endings = [
    "I adore you endlessly ❤️",
    "I can't stop thinking about you 💕",
    "you mean more to me than words can say 💖",
    "stay close to my heart forever 💘",
    "you are my forever and always 💞",
    "I cherish you deeply 💓",
    "you make my world complete 💝",
    "I fall for you more every day 💗",
    "my heart belongs to you 💟",
    "I love you beyond the stars ✨"
]

# Generate personalized romantic message
def generate_romantic_message(name: str):
    opening = random.choice(openings).format(name=name)
    middle = random.choice(middles)
    ending = random.choice(endings)
    return f"{opening} {middle} {ending}"

# Handle incoming messages
def handle_message(update: Update, context=None):
    chat_id = update.effective_chat.id
    first_name = update.effective_user.first_name or "Love"
    
    # Remember user's name
    user_names[chat_id] = first_name
    
    # Send personalized message
    reply = generate_romantic_message(first_name)
    update.message.reply_text(reply)

dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Flask route for webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

# Set webhook automatically when app starts
@app.before_first_request
def set_webhook():
    bot.set_webhook(f"{WEBHOOK_URL}/{TOKEN}")

# Health check route
@app.route("/", methods=["GET"])
def index():
    return "Romance Bot is alive 💖"

if __name__ == "__main__":
    app.run(debug=True)
