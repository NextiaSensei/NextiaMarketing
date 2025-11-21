import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
EMAIL = os.getenv("EMAIL_CONTACTO")
WEB1 = os.getenv("WEBSITE_1")
WEB2 = os.getenv("WEBSITE_2")
WEB3 = os.getenv("WEBSITE_3")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

MESSAGES = {
    "presale": f"""
🚀 **NEXTIA TOKEN - PRESALE TIER 1**

📊 Supply Total: 1M NXT
💰 APY Staking: 20%
✅ Smart Contracts: 16/16 Tests Pasando
🔐 Audited: NextiaData

**Únete a la presale:**
https://nextia-marketing.vercel.app

**Ecosistema Nextia Marketing y Token:**
🔗 {WEB1}
🔗 {WEB2}
🔗 {WEB3}

📧 Email: {EMAIL}

🔗 Telegram: https://t.me/nextiatoken_presale_bot.
""",
    
    "trading": """
🤖 **SEÑAL DE TRADING - NEXTIA**

📈 Par: NXT/USDT
💹 Entrada: $0.005
🎯 Target: $0.01
⛔ Stop Loss: $0.003

⏱️ Risk/Reward: 1:2
📊 Confianza: 85%
""",
    
    "staking": f"""
💰 **NEXTIA STAKING**

🎯 APY: 20% anual
⏸️ Sin lock-up
🔄 Rewards cada bloque

🔗 Staking live en: {WEB2}
📧 Contacto: {EMAIL}
""",
}

@bot.event
async def on_ready():
    print(f"✅ Bot Discord conectado como {bot.user}")
    print(f"📧 Email: {EMAIL}")
    print(f"Comandos: !presale, !trading, !staking, !custom")
    
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        try:
            await channel.send("🚀 **BOT NEXTIA ACTIVADO** - Usa !presale, !trading, !staking")
        except:
            pass

@bot.command(name="presale")
async def presale(ctx):
    """Publica info de presale"""
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    await channel.send(MESSAGES["presale"])

@bot.command(name="trading")
async def trading(ctx):
    """Publica señal de trading"""
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    await channel.send(MESSAGES["trading"])

@bot.command(name="staking")
async def staking(ctx):
    """Publica info de staking"""
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    await channel.send(MESSAGES["staking"])

@bot.command(name="custom")
async def custom(ctx, *, texto):
    """Mensaje personalizado"""
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    await channel.send(texto)

print("🤖 Bot Discord iniciado...")
bot.run(DISCORD_BOT_TOKEN)

