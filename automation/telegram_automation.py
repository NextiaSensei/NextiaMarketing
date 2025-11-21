import telebot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
EMAIL = os.getenv("EMAIL_CONTACTO")
WEB1 = os.getenv("WEBSITE_1")
WEB2 = os.getenv("WEBSITE_2")
WEB3 = os.getenv("WEBSITE_3")

bot = telebot.TeleBot(BOT_TOKEN)

MESSAGES = {
    "presale": f"""
🚀 NEXTIA TOKEN - PRESALE TIER 1

📊 Supply Total: 1M NXT
💰 APY Staking: 20%
✅ Smart Contracts: 16/16 Tests Pasando
🔐 Audited: NextiaData

Únete al PreSale
🔗 https://nextia-marketing.vercel.app

Ecosistema Nextia Marketing:
🔗 {WEB1}
🔗 {WEB2}
🔗 {WEB3}

📧 Email: {EMAIL}

GibHub: https://github.com/NextiaSensei
Discord: https://discord.gg/PtWWkpfC
""",
    
    "trading": """
🤖 SEÑAL DE TRADING - NEXTIA

📈 Par: NXT/USDT
💹 Entrada: $0.005
🎯 Target: $0.01
⛔ Stop Loss: $0.003

⏱️ Risk/Reward: 1:2
📊 Confianza: 85%

Seguir updates en Telegram
""",
    
    "staking": f"""
💰 NEXTIA STAKING

🎯 APY: 20% anual
⏸️ Sin lock-up
🔄 Rewards cada bloque
📊 Sostenible basado en revenue real

Staking live en: {WEB2}

📧 Contacto: {EMAIL}

#DeFi #Staking #NextiaToken
"""
}

@bot.message_handler(commands=['start'])
def start(message):
    text = """
👋 Hola! Soy el bot de Nextia Token

COMANDOS:
/presale - Info de presale
/trading - Señal de trading
/staking - Info de staking
/web1 - nextiamarketing.co
/web2 - tokenlab.nextiamarketing.com
/web3 - shoplab.nextiamarketing.com
/help - Ayuda
/custom "mensaje" - Mensaje personalizado
"""
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['presale'])
def presale(message):
    bot.send_message(CHANNEL_ID, MESSAGES["presale"])
    bot.send_message(message.chat.id, "✅ Presale publicada!")

@bot.message_handler(commands=['trading'])
def trading(message):
    bot.send_message(CHANNEL_ID, MESSAGES["trading"])
    bot.send_message(message.chat.id, "✅ Señal publicada!")

@bot.message_handler(commands=['staking'])
def staking(message):
    bot.send_message(CHANNEL_ID, MESSAGES["staking"])
    bot.send_message(message.chat.id, "✅ Staking info publicada!")

@bot.message_handler(commands=['web1'])
def web1(message):
    text = f"🔗 Presale oficial:\n{WEB1}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['web2'])
def web2(message):
    text = f"🔗 Staking & TokenLab:\n{WEB2}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['web3'])
def web3(message):
    text = f"🔗 Shop & Recursos:\n{WEB3}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['custom'])
def custom(message):
    text = message.text.replace('/custom ', '', 1).strip()
    if text:
        bot.send_message(CHANNEL_ID, text)
        bot.send_message(message.chat.id, f"✅ Publicado: {text}")
    else:
        bot.send_message(message.chat.id, "❌ Uso: /custom Tu mensaje")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    text = """
📚 AYUDA

/presale - Presale info
/trading - Trading signal
/staking - Staking info
/web1 - nextiamarketing.co
/web2 - tokenlab
/web3 - shoplab
/custom "texto" - Tu mensaje
/help - Esto
"""
    bot.send_message(message.chat.id, text)

print("🤖 Bot Telegram iniciado - Escuchando comandos...")
print(f"📧 Email: {EMAIL}")
print(f"🌐 Sitios: {WEB1}, {WEB2}, {WEB3}")
bot.infinity_polling()

