"""
Script de automatización de Twitter/X para Nextia Token
Publica tweets automáticamente sobre presale, staking, y actualizaciones

Requerimientos:
    pip install tweepy python-dotenv

Uso:
    python twitter_automation.py --tweet "Tu tweet aquí"
    python twitter_automation.py --thread archivo.txt
    python twitter_automation.py --presale
    python twitter_automation.py --staking
    python twitter_automation.py --community
"""

import tweepy
import os
from dotenv import load_dotenv
import argparse
from datetime import datetime
import time
import schedule

load_dotenv()

# ====== CONFIGURACIÓN ======
CONSUMER_KEY = os.getenv("TWITTER_API_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

EMAIL = os.getenv("EMAIL_CONTACTO")
WEB1 = os.getenv("WEBSITE_1")
WEB2 = os.getenv("WEBSITE_2")
WEB3 = os.getenv("WEBSITE_3")

# Inicializar cliente
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# ====== FUNCIONES ======

def post_single_tweet(text):
    """Publica un tweet individual"""
    try:
        response = client.create_tweet(text=text)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"✅ [{timestamp}] Tweet publicado")
        print(f"   ID: {response.data['id']}")
        print(f"   Texto: {text[:50]}...\n")
        return response.data['id']
    except Exception as e:
        print(f"❌ Error: {e}\n")
        return None

def post_thread(tweets_list):
    """Publica un thread"""
    try:
        previous_id = None
        for i, tweet_text in enumerate(tweets_list, 1):
            response = client.create_tweet(
                text=tweet_text,
                in_reply_to_tweet_id=previous_id
            )
            print(f"✅ Tweet {i}/{len(tweets_list)} publicado")
            previous_id = response.data['id']
            time.sleep(2)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n✅ [{timestamp}] Thread completado\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def post_scheduled(hour, minute, text):
    """Agenda un tweet diario"""
    def job():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n📍 [{timestamp}] Publicando tweet programado...")
        post_single_tweet(text)
    
    schedule_time = f"{hour:02d}:{minute:02d}"
    schedule.every().day.at(schedule_time).do(job)
    
    print(f"⏰ Tweet programado para las {schedule_time} UTC diariamente")
    print(f"   Mensaje: {text[:60]}...\n")
    
    while True:
        schedule.run_pending()
        time.sleep(60)

# ====== TWEETS PREDEFINIDOS ======

PRESALE_TWEETS = [
    f"""🚀 ¡NEXTIA TOKEN PRESALE LIVE!

✅ Tier 1: $0.005 (-40% descuento)
✅ 20% APY Staking sin lock-up
✅ 4 Smart Contracts auditados
✅ Revenue real = Yields sostenibles

Únete: {WEB1}
Telegram: https://t.me/NextiaPresale

#DeFi #Token #Presale""",
    
    f"""¿Por qué Nextia Token?

1️⃣ Utilidad REAL (no vaporware)
2️⃣ Revenue compartido con holders
3️⃣ 20% APY staking sin lock-up
4️⃣ Governance descentralizado
5️⃣ Smart contracts 100% auditados

Whitelist: {WEB1}

#DeFi #Crypto #NextiaToken""",
    
    f"""FAQ - Nextia Token

❓ ¿Es seguro?
✅ 16/16 tests passing. Código en GitHub.

❓ ¿Cuándo mainnet?
✅ Q1 2026 después de auditoría.

❓ ¿APY garantizado?
✅ Basado en ingresos reales de la plataforma.

Discord: https://discord.gg/nextia

#DeFi #FAQ""",
    
    f"""🤖 Nextia Trading Bot

50+ usuarios activos
Signals automáticas en Telegram
ML optimization en tiempo real

📊 Próximamente integrado en DApp

Discord: https://discord.gg/nextia
Email: {EMAIL}

#TradingBot #Signals""",
]

STAKING_TWEETS = [
    f"""📊 Staking 101 con Nextia

✅ Sin lock-up
✅ Claim rewards cuando quieras
✅ 20% APY sostenible
✅ Calculada por segundo
✅ Basada en ingresos reales

No es un ponzi. Es tokenomics real.

Staking: {WEB2}

#DeFi #Staking""",
    
    f"""¿Cómo los yields son sostenibles?

Nextia genera ingresos REALES:
- 50% → Stakers (rewards)
- 25% → Desarrollo
- 25% → Operaciones

Transparencia total en DAO governance.

Staking: {WEB2}

#DeFi #Transparency""",
    
    f"""APY 20% en Nextia

Semanal: 0.38% (~$3.80 por $1000)
Mensual: 1.67% (~$16.70 por $1000)
Anual: 20% (~$200 por $1000)

Sin vesting. Sin lock-up.
Claim cuando quieras.

{WEB2}

#DeFi #Yields""",
]

COMMUNITY_TWEETS = [
    f"""¡Únete a Nextia! 🌍

💬 Telegram: https://t.me/NextiaPresale
💎 Discord: https://discord.gg/nextia
📂 GitHub: https://github.com/NextiaLabs
📧 Email: {EMAIL}

Vamos a construir esto juntos.

#Community #DeFi""",
    
    f"""Roadmap Nextia Token 2025

Q4 2025: Presale + Staking beta
Q1 2026: Mainnet launch + auditoría
Q2 2026: Trading bot v2 + partnerships
Q3 2026: 10K+ holders target
Q4 2026: Top 100 DeFi protocols

Únete: {WEB1}

#Roadmap #DeFi""",
]

# ====== MAIN ======

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Twitter Bot - Nextia Token")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--tweet", help="Tweet individual")
    group.add_argument("--thread", help="Thread desde archivo")
    group.add_argument("--presale", action="store_true", help="Tweets presale")
    group.add_argument("--staking", action="store_true", help="Tweets staking")
    group.add_argument("--community", action="store_true", help="Tweets comunidad")
    group.add_argument("--all", action="store_true", help="Todos los tweets")
    group.add_argument("--schedule", nargs=2, metavar=("TIME", "TEXT"), help="Agendar tweet")
    
    args = parser.parse_args()
    
    if args.tweet:
        post_single_tweet(args.tweet)
    
    elif args.thread:
        try:
            with open(args.thread, 'r', encoding='utf-8') as f:
                tweets = [line.strip() for line in f if line.strip()]
            if tweets:
                post_thread(tweets)
            else:
                print("❌ Archivo vacío\n")
        except FileNotFoundError:
            print(f"❌ Archivo no encontrado\n")
    
    elif args.presale:
        print("📢 Publicando tweets presale...\n")
        for tweet in PRESALE_TWEETS:
            post_single_tweet(tweet)
            time.sleep(3)
    
    elif args.staking:
        print("📊 Publicando tweets staking...\n")
        for tweet in STAKING_TWEETS:
            post_single_tweet(tweet)
            time.sleep(3)
    
    elif args.community:
        print("🌍 Publicando tweets comunidad...\n")
        for tweet in COMMUNITY_TWEETS:
            post_single_tweet(tweet)
            time.sleep(3)
    
    elif args.all:
        print("🚀 Publicando TODOS los tweets...\n")
        all_tweets = PRESALE_TWEETS + STAKING_TWEETS + COMMUNITY_TWEETS
        for tweet in all_tweets:
            post_single_tweet(tweet)
            time.sleep(3)
    
    elif args.schedule:
        time_str, text = args.schedule
        try:
            hour, minute = map(int, time_str.split(':'))
            post_scheduled(hour, minute, text)
        except ValueError:
            print("❌ Formato inválido. Usa HH:MM (ej: 09:00)\n")
    
    else:
        print("❌ Especifica: --tweet, --thread, --presale, --staking, --community, --all, o --schedule\n")
        parser.print_help()

