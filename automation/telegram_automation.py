import telebot
import os
import schedule
import time
import threading
from datetime import datetime
from telebot import types
from dotenv import load_dotenv

# ─────────────────────────────────────────
# LOAD ENV
# ─────────────────────────────────────────

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
EMAIL = os.getenv("EMAIL_CONTACTO")
WEB1 = os.getenv("WEBSITE_1")
WEB2 = os.getenv("WEBSITE_2")
WEB3 = os.getenv("WEBSITE_3")

if not BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN no encontrado en .env")

if not CHANNEL_ID:
    raise ValueError("❌ TELEGRAM_CHANNEL_ID no encontrado en .env")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="Markdown")

# ─────────────────────────────────────────
# MENSAJES OPTIMIZADOS
# ─────────────────────────────────────────

MSG = {

    "presale": f"""
🚀 *NEXTIA TOKEN — PRESALE TIER 1*

━━━━━━━━━━━━━━━━━━━
⚡ *Estado actual*
• ERC-20 desplegado en Sepolia
• Smart Contracts funcionando
• 16/16 Tests pasando ✅
• Preparación para Ethereum Mainnet

━━━━━━━━━━━━━━━━━━━
🌐 *¿Qué es Nextia?*

Nextia es un ecosistema Web3 enfocado en:

🤖 Trading Bots IA  
🧪 Herramientas para creación de tokens  
📊 Simuladores DeFi  
🏛️ Gobernanza DAO  
💎 Infraestructura escalable para builders

━━━━━━━━━━━━━━━━━━━
🎯 *Objetivo de la Presale*

Construir liquidez sólida, desarrollo sostenible
y expansión del ecosistema.

━━━━━━━━━━━━━━━━━━━
🔗 Presale:
{WEB1}

🔗 Ecosistema:
{WEB2}

📂 GitHub:
https://github.com/NextiaSensei

📧 Contacto:
{EMAIL}
""",

    "ecosistema": f"""
🌐 *ECOSISTEMA NEXTIA*

━━━━━━━━━━━━━━━━━━━
1️⃣ *NXT Token (ERC-20)*

• Contratos desplegados
• Tests completados
• Arquitectura preparada para Mainnet

━━━━━━━━━━━━━━━━━━━
2️⃣ *TokenLab*

Herramientas para:

🧪 Simular inversión  
🔧 Crear proyectos Web3  
🚀 Escalar ecosistemas digitales

━━━━━━━━━━━━━━━━━━━
3️⃣ *Trading Bots IA*

Bots conectados a:

📈 MetaTrader 5  
📊 Binance  
⚙️ Estrategias algorítmicas

Con meses de pruebas y optimización.

━━━━━━━━━━━━━━━━━━━
4️⃣ *Gobernanza DAO*

La visión es migrar hacia decisiones
más descentralizadas y transparentes.

━━━━━━━━━━━━━━━━━━━
🔗 Explorar:
{WEB2}
""",

    "trading_bot": f"""
🤖 *NEXTIA TRADING BOTS*

━━━━━━━━━━━━━━━━━━━
⚙️ Infraestructura actual

• MetaTrader 5
• Binance
• Automatización algorítmica
• Backtesting y pruebas demo

━━━━━━━━━━━━━━━━━━━
📊 Objetivo

Construir sistemas de trading:

✅ Escalables  
✅ Transparentes  
✅ Basados en datos  
✅ En mejora continua

━━━━━━━━━━━━━━━━━━━
📌 Importante

Los resultados históricos NO garantizan
resultados futuros.

Todo el desarrollo se encuentra en fase
de investigación y optimización.

━━━━━━━━━━━━━━━━━━━
🔗 Simulador:
tokenlab.nextiamarketing.com/simulador-de-inversion-crypto/

🔗 Ecosistema:
{WEB2}
""",

    "staking": f"""
💰 *NEXTIA STAKING*

━━━━━━━━━━━━━━━━━━━
⚡ El sistema de staking todavía se
encuentra en desarrollo y validación.

No se promete rendimiento fijo.

━━━━━━━━━━━━━━━━━━━
🎯 Objetivo del modelo:

• Sostenibilidad
• Transparencia
• Recompensas reales
• Integración con revenue futuro

━━━━━━━━━━━━━━━━━━━
📌 Filosofía Nextia:

Primero construir infraestructura sólida.
Después escalar el ecosistema.

━━━━━━━━━━━━━━━━━━━
🔗 Más información:
{WEB2}

📧 Contacto:
{EMAIL}
""",

    "tokenlab": f"""
🧪 *TOKENLAB*

━━━━━━━━━━━━━━━━━━━
Herramientas Web3 para builders.

━━━━━━━━━━━━━━━━━━━
⚙️ Roadmap actual

✅ Landing del ecosistema  
✅ Simulador de inversión  
🔄 Herramientas de automatización  
🔜 Creator de Tokens  
🔜 Launchpad

━━━━━━━━━━━━━━━━━━━
🎯 Visión

Facilitar la creación de proyectos
crypto sin complicar la experiencia.

━━━━━━━━━━━━━━━━━━━
🔗 Plataforma:
{WEB2}
""",

    "noticias_crypto": """
📰 *NEXTIA CRYPTO DIGEST*

━━━━━━━━━━━━━━━━━━━
🌍 Tendencias actuales del mercado:

• Crecimiento de herramientas IA
• Expansión de ecosistemas DeFi
• Más adopción de automatización
• Infraestructura Web3 más madura

━━━━━━━━━━━━━━━━━━━
📌 En Nextia seguimos construyendo:

⚙️ Tecnología
📊 Automatización
🧪 Herramientas
🌐 Ecosistema

Paso a paso. Sin humo.
""",

    "transparencia": f"""
🔍 *NEXTIA — TRANSPARENCIA*

━━━━━━━━━━━━━━━━━━━
📌 Lo que sí existe hoy:

✅ Smart Contracts en Sepolia  
✅ Código abierto  
✅ Tests automatizados  
✅ Bots en pruebas demo  
✅ Landing y simuladores funcionales

━━━━━━━━━━━━━━━━━━━
📂 GitHub:
https://github.com/NextiaSensei

🔗 Ecosistema:
{WEB2}

📧 Contacto:
{EMAIL}
""",

    "comunidad": f"""
👥 *COMUNIDAD NEXTIA*

━━━━━━━━━━━━━━━━━━━
No buscamos solo holders.

Buscamos builders ⚡

━━━━━━━━━━━━━━━━━━━
Puedes participar como:

💻 Developer  
📈 Trader  
🎨 Diseñador  
📢 Marketer  
🧠 Estratega  
🚀 Inversionista

━━━━━━━━━━━━━━━━━━━
📣 Canales oficiales

Telegram:
Este canal

Discord:
https://discord.gg/PtWWkpfC

GitHub:
https://github.com/NextiaSensei

━━━━━━━━━━━━━━━━━━━
🌐 Ecosistema:
{WEB2}
"""
}

# ─────────────────────────────────────────
# MENU
# ─────────────────────────────────────────

def menu_principal():

    markup = types.InlineKeyboardMarkup(row_width=2)

    buttons = [
        types.InlineKeyboardButton("🚀 Presale", callback_data="presale"),
        types.InlineKeyboardButton("🌐 Ecosistema", callback_data="ecosistema"),

        types.InlineKeyboardButton("🤖 Trading Bots", callback_data="trading_bot"),
        types.InlineKeyboardButton("💰 Staking", callback_data="staking"),

        types.InlineKeyboardButton("🧪 TokenLab", callback_data="tokenlab"),
        types.InlineKeyboardButton("📰 Crypto News", callback_data="noticias_crypto"),

        types.InlineKeyboardButton("🔍 Transparencia", callback_data="transparencia"),
        types.InlineKeyboardButton("👥 Comunidad", callback_data="comunidad"),

        types.InlineKeyboardButton("🌐 Web", url=WEB2),
        types.InlineKeyboardButton("📂 GitHub", url="https://github.com/NextiaSensei")
    ]

    markup.add(*buttons)

    return markup

# ─────────────────────────────────────────
# START
# ─────────────────────────────────────────

@bot.message_handler(commands=['start', 'menu'])
def start(message):

    text = f"""
👋 *Bienvenido al Ecosistema Nextia*

Construyendo herramientas Web3,
automatización e infraestructura crypto.

━━━━━━━━━━━━━━━━━━━
Selecciona una sección:
"""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=menu_principal()
    )

# ─────────────────────────────────────────
# COMMANDS
# ─────────────────────────────────────────

@bot.message_handler(commands=['presale'])
def presale(message):
    bot.send_message(message.chat.id, MSG["presale"])

@bot.message_handler(commands=['ecosistema'])
def ecosistema(message):
    bot.send_message(message.chat.id, MSG["ecosistema"])

@bot.message_handler(commands=['trading'])
def trading(message):
    bot.send_message(message.chat.id, MSG["trading_bot"])

@bot.message_handler(commands=['staking'])
def staking(message):
    bot.send_message(message.chat.id, MSG["staking"])

@bot.message_handler(commands=['tokenlab'])
def tokenlab(message):
    bot.send_message(message.chat.id, MSG["tokenlab"])

@bot.message_handler(commands=['news'])
def news(message):
    bot.send_message(message.chat.id, MSG["noticias_crypto"])

@bot.message_handler(commands=['transparencia'])
def transparencia(message):
    bot.send_message(message.chat.id, MSG["transparencia"])

@bot.message_handler(commands=['comunidad'])
def comunidad(message):
    bot.send_message(message.chat.id, MSG["comunidad"])

# ─────────────────────────────────────────
# PUBLICAR
# ─────────────────────────────────────────

@bot.message_handler(commands=['publicar'])
def publicar(message):

    bot.send_message(
        CHANNEL_ID,
        MSG["presale"]
    )

    bot.send_message(
        message.chat.id,
        "✅ Publicación enviada al canal"
    )

# ─────────────────────────────────────────
# ESTADO
# ─────────────────────────────────────────

@bot.message_handler(commands=['estado'])
def estado(message):

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    text = f"""
⚙️ *ESTADO DEL SISTEMA*

━━━━━━━━━━━━━━━━━━━
🟢 Bot activo

📅 Fecha:
{ahora}

🌐 WEB:
{WEB2}

📂 GitHub:
https://github.com/NextiaSensei

━━━━━━━━━━━━━━━━━━━
✅ Smart Contracts operativos
✅ Tests funcionando
✅ Scheduler activo
"""

    bot.send_message(message.chat.id, text)

# ─────────────────────────────────────────
# HELP
# ─────────────────────────────────────────

@bot.message_handler(commands=['help'])
def help_command(message):

    text = """
📚 *COMANDOS*

/menu
/presale
/ecosistema
/trading
/staking
/tokenlab
/news
/transparencia
/comunidad
/estado
/publicar
"""

    bot.send_message(message.chat.id, text)

# ─────────────────────────────────────────
# CALLBACKS
# ─────────────────────────────────────────

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    if call.data in MSG:

        bot.answer_callback_query(call.id)

        bot.send_message(
            call.message.chat.id,
            MSG[call.data]
        )

# ─────────────────────────────────────────
# AUTO PUBLICACIONES
# ─────────────────────────────────────────

def auto_publish_presale():

    bot.send_message(CHANNEL_ID, MSG["presale"])

    print(f"✅ Presale publicada — {datetime.now()}")

def auto_publish_ecosistema():

    bot.send_message(CHANNEL_ID, MSG["ecosistema"])

    print(f"✅ Ecosistema publicado — {datetime.now()}")

def auto_publish_transparencia():

    bot.send_message(CHANNEL_ID, MSG["transparencia"])

    print(f"✅ Transparencia publicada — {datetime.now()}")

def run_scheduler():

    schedule.every().day.at("09:00").do(auto_publish_presale)
    schedule.every().day.at("18:00").do(auto_publish_presale)

    schedule.every().monday.at("11:00").do(auto_publish_ecosistema)

    schedule.every().friday.at("12:00").do(auto_publish_transparencia)

    while True:
        schedule.run_pending()
        time.sleep(60)

# ─────────────────────────────────────────
# THREAD
# ─────────────────────────────────────────

scheduler_thread = threading.Thread(
    target=run_scheduler,
    daemon=True
)

scheduler_thread.start()

# ─────────────────────────────────────────
# INIT
# ─────────────────────────────────────────

print("🤖 NEXTIA TELEGRAM BOT ONLINE")
print(f"🌐 {WEB2}")
print("📅 Scheduler activo")

bot.infinity_polling(skip_pending=True)
