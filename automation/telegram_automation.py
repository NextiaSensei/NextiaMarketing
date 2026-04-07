import telebot
import os
import schedule
import time
import threading
from datetime import datetime
from telebot import types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
EMAIL = os.getenv("EMAIL_CONTACTO")
WEB1 = os.getenv("WEBSITE_1")
WEB2 = os.getenv("WEBSITE_2")
WEB3 = os.getenv("WEBSITE_3")

bot = telebot.TeleBot(BOT_TOKEN)

# ─────────────────────────────────────────
# MENSAJES DEL ECOSISTEMA
# ─────────────────────────────────────────

MSG = {
    "presale": f"""
🚀 *NEXTIA TOKEN — PRESALE TIER 1*

📊 Supply Total: *1,000,000 NXT*
💰 APY Staking: *20% anual*
✅ Smart Contracts: *16/16 Tests Pasando*
🔐 Auditado: NextiaData
🌐 Red: *Sepolia Testnet → Mainnet próximamente*

━━━━━━━━━━━━━━━━━━━━
💡 ¿Por qué entrar en Fase 1?
• Precio de entrada más bajo del ciclo
• Acceso prioritario al ecosistema completo
• Participación en gobernanza DAO

🔗 Únete ahora: [nextia-marketing.vercel.app](https://nextia-marketing.vercel.app)
🔗 TokenLab: {WEB2}

📧 {EMAIL}
""",

    "ecosistema": f"""
🌐 *ECOSISTEMA NEXTIA TOKEN*

El ecosistema está compuesto por 4 pilares:

1️⃣ *NXT Token (ERC-20)*
   Smart contracts auditados en Sepolia
   Listo para mainnet

2️⃣ *Staking & Gobernanza*
   20% APY · Sin lock-up · Rewards por bloque
   Votación descentralizada activa

3️⃣ *TokenLab*
   Plataforma para crear y lanzar tokens propios
   Con simulador de inversión integrado

4️⃣ *Trading Bots IA*
   Bot activo en MetaTrader 5 + Binance
   *+5 meses de datos reales en demo*
   Peak: $8,929 | Ganancia: $128.91

🔗 Explorar: {WEB2}
📂 GitHub: [NextiaSensei](https://github.com/NextiaSensei)
""",

    "trading_bot": """
🤖 *REPORTE: TRADING BOT NEXTIA*

📅 Período de prueba: *+5 meses*
⚙️ Plataformas: MetaTrader 5 + Binance

📊 *Resultados Demo:*
• Peak (mejor balance): $8,929.06
• Ganancia al peak: +$128.91
• Balance final: $8,207.15
• Retorno al peak: +1.46%
• Drawdown máximo: -8.08%

✅ *4 símbolos activos*
✅ *6 operaciones analizadas*
✅ Datos sin esconder — transparencia total

🔗 Ver simulador en vivo: tokenlab.nextiamarketing.com/simulador-de-inversion-crypto/
""",

    "staking": f"""
💰 *NEXTIA STAKING — DEFI REAL*

🎯 APY: *20% anual*
⏸️ Sin lock-up (retira cuando quieras)
🔄 Rewards calculados cada bloque
📊 Sostenible: basado en revenue real del ecosistema

━━━━━━━━━━━━━━━━━━━━
🧮 *Ejemplo de rendimiento:*
• $1,000 invertidos → +$200/año
• $5,000 invertidos → +$1,000/año
• $10,000 invertidos → +$2,000/año

🔗 Staking live: {WEB2}
📧 Consultas: {EMAIL}
""",

    "tokenlab": f"""
🧪 *TOKENLAB — CREA TU PROPIO TOKEN*

TokenLab es la plataforma del ecosistema Nextia para:

🔧 Crear tokens ERC-20 sin código
📊 Simular rendimientos de inversión
🚀 Lanzar tu presale paso a paso
📈 Conectar con bots de trading IA

*Roadmap TokenLab:*
├── ✅ Simulador de Inversión (LIVE)
├── ✅ Landing Page del Ecosistema (LIVE)
├── 🔄 Creator de Tokens (Q2 2026)
└── 🔜 Launchpad Público (Q3 2026)

🔗 Explorar ahora: {WEB2}
📂 Código abierto: [GitHub](https://github.com/NextiaSensei)
""",

    "noticias_crypto": """
📰 *CRIPTO NEWS — NEXTIA DIGEST*

💡 El mercado DeFi sigue creciendo:
• Total Value Locked (TVL) en DeFi supera los $100B
• Ethereum Sepolia es la testnet más usada para ERC-20
• Los bots de trading algorítmico ganan terreno en retail

🎯 *¿Cómo afecta a Nextia Token?*
Nuestros contratos están en Sepolia y listos para mainnet.
Los bots de trading llevan +5 meses de pruebas reales.
Entramos en un momento óptimo del mercado.

🔗 Más info: tokenlab.nextiamarketing.com
""",

    "transparencia": f"""
🔍 *NEXTIA TOKEN — TRANSPARENCIA TOTAL*

No escondemos nada. Aquí los datos reales:

✅ Smart Contracts: 16/16 tests pasando
✅ Código abierto en GitHub
✅ Bot de trading: datos demo públicos
✅ Drawdown real publicado (-8.08%)
✅ Whitepaper completo disponible

📂 Revisa todo tú mismo:
• GitHub: [NextiaSensei](https://github.com/NextiaSensei)
• Simulador: tokenlab.nextiamarketing.com/simulador-de-inversion-crypto/
• Ecosistema: {WEB2}

📧 Preguntas directas: {EMAIL}
""",

    "comunidad": f"""
👥 *ÚNETE A LA COMUNIDAD NEXTIA*

Somos builders, no solo inversores:

🤝 ¿Qué puedes hacer aquí?
• Invertir en Presale Tier 1
• Participar en gobernanza DAO
• Contribuir al código (GitHub abierto)
• Usar TokenLab para tu propio proyecto
• Seguir el desarrollo de los trading bots

📣 Canales oficiales:
• Telegram: este canal
• Discord: [discord.gg/PtWWkpfC](https://discord.gg/PtWWkpfC)
• GitHub: [NextiaSensei](https://github.com/NextiaSensei)

🔗 Ecosistema: {WEB2}
📧 Email: {EMAIL}
"""
}

# ─────────────────────────────────────────
# MENÚ PRINCIPAL CON INLINE BUTTONS
# ─────────────────────────────────────────

def menu_principal():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🚀 Presale Info", callback_data="presale"),
        types.InlineKeyboardButton("🌐 Ecosistema", callback_data="ecosistema"),
        types.InlineKeyboardButton("🤖 Trading Bot", callback_data="trading_bot"),
        types.InlineKeyboardButton("💰 Staking", callback_data="staking"),
        types.InlineKeyboardButton("🧪 TokenLab", callback_data="tokenlab"),
        types.InlineKeyboardButton("📰 Cripto News", callback_data="noticias_crypto"),
        types.InlineKeyboardButton("🔍 Transparencia", callback_data="transparencia"),
        types.InlineKeyboardButton("👥 Comunidad", callback_data="comunidad"),
        types.InlineKeyboardButton("🔗 Ir al TokenLab", url=WEB2),
        types.InlineKeyboardButton("📂 GitHub", url="https://github.com/NextiaSensei")
    )
    return markup

# ─────────────────────────────────────────
# HANDLERS DE COMANDOS
# ─────────────────────────────────────────

@bot.message_handler(commands=['start', 'menu'])
def start(message):
    text = """
👋 *Bienvenido al Bot Oficial de Nextia Token*

Soy tu guía completo del ecosistema. Aquí encontrarás:

🚀 Info de Presale Tier 1
🌐 Todo sobre el Ecosistema Nextia
🤖 Resultados de los Trading Bots IA
💰 Staking con 20% APY
🧪 TokenLab — crea tu propio token
📰 Noticias del mundo crypto
🔍 Datos transparentes y verificables

Selecciona una opción:
"""
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=menu_principal())

@bot.message_handler(commands=['presale'])
def cmd_presale(message):
    bot.send_message(message.chat.id, MSG["presale"], parse_mode="Markdown")

@bot.message_handler(commands=['ecosistema'])
def cmd_ecosistema(message):
    bot.send_message(message.chat.id, MSG["ecosistema"], parse_mode="Markdown")

@bot.message_handler(commands=['trading'])
def cmd_trading(message):
    bot.send_message(message.chat.id, MSG["trading_bot"], parse_mode="Markdown")

@bot.message_handler(commands=['staking'])
def cmd_staking(message):
    bot.send_message(message.chat.id, MSG["staking"], parse_mode="Markdown")

@bot.message_handler(commands=['tokenlab'])
def cmd_tokenlab(message):
    bot.send_message(message.chat.id, MSG["tokenlab"], parse_mode="Markdown")

@bot.message_handler(commands=['news'])
def cmd_news(message):
    bot.send_message(message.chat.id, MSG["noticias_crypto"], parse_mode="Markdown")

@bot.message_handler(commands=['transparencia'])
def cmd_transparencia(message):
    bot.send_message(message.chat.id, MSG["transparencia"], parse_mode="Markdown")

@bot.message_handler(commands=['comunidad'])
def cmd_comunidad(message):
    bot.send_message(message.chat.id, MSG["comunidad"], parse_mode="Markdown")

@bot.message_handler(commands=['publicar'])
def cmd_publicar(message):
    """Publica el menú completo en el canal"""
    bot.send_message(CHANNEL_ID, MSG["presale"], parse_mode="Markdown")
    bot.send_message(message.chat.id, "✅ Presale publicada en el canal!")

@bot.message_handler(commands=['publicar_ecosistema'])
def cmd_publicar_ecosistema(message):
    bot.send_message(CHANNEL_ID, MSG["ecosistema"], parse_mode="Markdown")
    bot.send_message(message.chat.id, "✅ Ecosistema publicado en el canal!")

@bot.message_handler(commands=['publicar_trading'])
def cmd_publicar_trading(message):
    bot.send_message(CHANNEL_ID, MSG["trading_bot"], parse_mode="Markdown")
    bot.send_message(message.chat.id, "✅ Reporte trading publicado!")

@bot.message_handler(commands=['custom'])
def cmd_custom(message):
    text = message.text.replace('/custom ', '', 1).strip()
    if text:
        bot.send_message(CHANNEL_ID, text, parse_mode="Markdown")
        bot.send_message(message.chat.id, f"✅ Publicado en canal: {text[:50]}...")
    else:
        bot.send_message(message.chat.id, "❌ Uso: /custom Tu mensaje en *Markdown*")

@bot.message_handler(commands=['estado'])
def cmd_estado(message):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"""
⚙️ *ESTADO DEL SISTEMA*

🟢 Bot: Activo
📅 Fecha: {ahora}
🌐 TokenLab: {WEB2}
🌐 Presale: {WEB1}
📧 Email: {EMAIL}
🔗 GitHub: github.com/NextiaSensei

*Smart Contracts:* 16/16 ✅
*Red actual:* Sepolia Testnet
*Trading Bot:* +5 meses datos
"""
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['help'])
def cmd_help(message):
    text = """
📚 *COMANDOS DISPONIBLES*

*Información:*
/menu — Menú interactivo completo
/presale — Info Presale Tier 1
/ecosistema — El ecosistema Nextia
/trading — Reporte Trading Bot IA
/staking — Info Staking 20% APY
/tokenlab — Plataforma TokenLab
/news — Noticias crypto
/transparencia — Datos verificables
/comunidad — Cómo unirte
/estado — Estado del sistema

*Publicar en canal:*
/publicar — Publica presale en canal
/publicar_ecosistema — Publica ecosistema
/publicar_trading — Publica reporte bot
/custom [texto] — Mensaje personalizado

*Links directos:*
/web1 — Presale oficial
/web2 — TokenLab
/web3 — ShopLab
"""
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['web1'])
def cmd_web1(message):
    bot.send_message(message.chat.id, f"🔗 *Presale Oficial:*\n{WEB1}", parse_mode="Markdown")

@bot.message_handler(commands=['web2'])
def cmd_web2(message):
    bot.send_message(message.chat.id, f"🔗 *TokenLab & Staking:*\n{WEB2}", parse_mode="Markdown")

@bot.message_handler(commands=['web3'])
def cmd_web3(message):
    bot.send_message(message.chat.id, f"🔗 *ShopLab:*\n{WEB3}", parse_mode="Markdown")

# ─────────────────────────────────────────
# CALLBACK PARA BOTONES INLINE
# ─────────────────────────────────────────

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data in MSG:
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, MSG[call.data], parse_mode="Markdown")
    bot.answer_callback_query(call.id)

# ─────────────────────────────────────────
# PUBLICACIONES AUTOMÁTICAS PROGRAMADAS
# ─────────────────────────────────────────

def auto_publish_presale():
    """Publica presale todos los días a las 9am y 6pm"""
    bot.send_message(CHANNEL_ID, MSG["presale"], parse_mode="Markdown")
    print(f"✅ Auto-publicado: Presale — {datetime.now()}")

def auto_publish_trading():
    """Publica reporte de trading cada lunes"""
    bot.send_message(CHANNEL_ID, MSG["trading_bot"], parse_mode="Markdown")
    print(f"✅ Auto-publicado: Trading — {datetime.now()}")

def auto_publish_ecosistema():
    """Publica ecosistema cada miércoles"""
    bot.send_message(CHANNEL_ID, MSG["ecosistema"], parse_mode="Markdown")
    print(f"✅ Auto-publicado: Ecosistema — {datetime.now()}")

def run_scheduler():
    schedule.every().day.at("09:00").do(auto_publish_presale)
    schedule.every().day.at("18:00").do(auto_publish_presale)
    schedule.every().monday.at("10:00").do(auto_publish_trading)
    schedule.every().wednesday.at("10:00").do(auto_publish_ecosistema)
    while True:
        schedule.run_pending()
        time.sleep(60)

# Corre el scheduler en un hilo separado
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

print("🤖 Bot Nextia Token — VERSIÓN OPTIMIZADA iniciado")
print(f"📧 Email: {EMAIL}")
print(f"🌐 Sitios: {WEB1} | {WEB2} | {WEB3}")
print("📅 Scheduler activo: 09:00, 18:00 diario + lunes/miércoles especiales")
bot.infinity_polling()
