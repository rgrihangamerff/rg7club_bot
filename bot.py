import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '8259886340:AAG4XNDPBumVBjPw7wATriYoYjpvWGSE3r8'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    first_name = message.from_user.first_name if message.from_user.first_name else "User"
    
    greeting_text = (
        f"👋 WELCOME TO THE WINNING CIRCLE!\n\n"
        f"💗 DEAR {first_name} WELCOME ABOARD!\n\n"
        f"🔰 YOU’VE JUST MET YOUR NEW ULTIMATE GAMING PARTNER — @RG7CLUB! 🤖\n"
        f"YOUR SMART ASSISTANT IS HERE TO:\n\n"
        f"✨ SIMPLIFY YOUR GAME: CLEAR UP ANY CONFUSION AND MASTER @RG7CLUB IN SECONDS.\n\n"
        f"🎁 DIRECT REWARDS: GET EXCLUSIVE PROMOTIONS, BONUSES, AND EVENT UPDATES PUSHED DIRECTLY TO YOU!\n\n"
        f"💸 UNLOCK EARNINGS: REVEAL THE SECRETS TO EARNING MONEY AS AN AGENT OR MEMBER.\n\n"
        f"SO... ARE YOU READY TO CONQUER THE WORLD OF @RG7CLUB ? 👇 JOIN US 👇"
    )

    markup = InlineKeyboardMarkup()
    
    markup.add(InlineKeyboardButton("🌐 OFFICIAL TELEGRAM CHANNEL ➢", url="https://t.me/+WNu_kNK5aqY0YTM1"))
    markup.add(InlineKeyboardButton("🟢 OFFICIAL WHATSAPP CHANNEL ✆", url="https://whatsapp.com/channel/0029VbCeBvD7oQhl0GaTrD15"))
    markup.add(InlineKeyboardButton("➢ CONTACT SUPPORT 👩🏻‍💻 (Telegram)", url="https://t.me/+919286012548"))
    markup.add(InlineKeyboardButton("✆ CONTACT SUPPORT 👩🏻‍💻 (WhatsApp)", url="https://wa.me/919286012548"))
    markup.add(InlineKeyboardButton("🅾 OFFICIAL INSTAGRAM", url="https://www.instagram.com/rg7club?igsh=NG1hZ2RhbXk2ZHly"))
    markup.add(InlineKeyboardButton("🔗 OFFICIAL DOMAIN", callback_data="show_domains"))

    bot.send_message(message.chat.id, greeting_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "show_domains")
def callback_domains(call):
    domain_text = (
        "🟩 **Official Domains**\n"
        "rg7club.xyz\n"
        "rg7club.com\n\n"
        "Only the above roots (and their subdomains) are official; everything else is treated as unofficial."
    )
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, domain_text, parse_mode="Markdown")

if __name__ == "__main__":
    bot.infinity_polling()
