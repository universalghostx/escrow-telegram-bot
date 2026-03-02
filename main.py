import telebot
from escrow import create_escrow, get_escrow, release_escrow, cancel_escrow, format_escrow

# ---------------- CONFIG ----------------
TOKEN = "8678864408:AAHhwuRxnuIXoubqgoBjd8vIlKbvYxWvRzQ"  # Replace with your BotFather token
bot = telebot.TeleBot(TOKEN)
# ---------------------------------------

# ---------- COMMANDS ----------

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Escrow Bot!\nUse /help to see commands.")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message,
    "/create <buyer> <seller> <amount> - Create an escrow (wallets auto-set)\n"
    "/status - Show current escrow\n"
    "/release - Release funds to seller\n"
    "/cancel - Cancel escrow")

@bot.message_handler(commands=['create'])
def create_command(message):
    try:
        args = message.text.split()
        if len(args) != 4:
            bot.reply_to(message, "Usage: /create <buyer> <seller> <amount>")
            return

        buyer, seller, amount = args[1], args[2], float(args[3])
        chat_id = message.chat.id

        escrow = create_escrow(chat_id, buyer, seller, amount)
        bot.reply_to(message, f"Escrow created!\n{format_escrow(escrow)}")
    except ValueError:
        bot.reply_to(message, "Amount must be a number.")

@bot.message_handler(commands=['status'])
def status_command(message):
    chat_id = message.chat.id
    escrow = get_escrow(chat_id)
    if escrow:
        bot.reply_to(message, format_escrow(escrow))
    else:
        bot.reply_to(message, "No active escrow found.")

@bot.message_handler(commands=['release'])
def release_command(message):
    chat_id = message.chat.id
    escrow = release_escrow(chat_id)
    if escrow:
        bot.reply_to(message, f"Funds released to seller!\n{format_escrow(escrow)}")
    else:
        bot.reply_to(message, "No active escrow found or funds already released.")

@bot.message_handler(commands=['cancel'])
def cancel_command(message):
    chat_id = message.chat.id
    if cancel_escrow(chat_id):
        bot.reply_to(message, "Escrow canceled.")
    else:
        bot.reply_to(message, "No active escrow to cancel.")

# ---------- RUN BOT ----------
print("Bot is running...")
bot.polling()
