"""
Script de automatización de Twitter/X para Nextia Token
Publica tweets automáticamente sobre presale, staking, y actualizaciones

Requerimientos:
    pip install tweepy python-dotenv

Uso:
    python twitter_automation.py --tweet "Tu tweet aquí"
    python twitter_automation.py --thread archivo.txt
    python twitter_automation.py --schedule 09:00 "Mensaje diario"
"""

import tweepy
import os
from dotenv import load_dotenv
import argparse
from datetime import datetime
import time
import schedule

load_dotenv()

# ====== CONFIGURACIÓN DE TWITTER API ======
CONSUMER_KEY = os.getenv("TWITTER_API_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

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
        print(f"✅ [{timestamp}] Tweet publicado exitosamente")
        print(f"   ID: {response.data['id']}")
        print(f"   Texto: {text[:60]}...")
        return response.data['id']
    except Exception as e:
        print(f"❌ Error al publicar tweet: {e}")
        return None

def post_thread(tweets_list):
    """Publica un thread de múltiples tweets"""
    try:
        previous_id = None
        for i, tweet_text in enumerate(tweets_list, 1):
            response = client.create_tweet(
                text=tweet_text,
                in_reply_to_tweet_id=previous_id
            )
            print(f"✅ Tweet {i}/{len(tweets_list)} publicado")
            previous_id = response.data['id']
            time.sleep(2)  # Esperar 2 segundos entre tweets
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n✅ [{timestamp}] Thread completado ({len(tweets_list)} tweets)")
    except Exception as e:
        print(f"❌ Error al publicar thread: {e}")

def post_scheduled(hour, minute, text):
    """Agenda un tweet para una hora específica"""
    def job():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n📍 [{timestamp}] Publicando tweet programado...")
        post_single_tweet(text)
    
    schedule_time = f"{hour:02d}:{minute:02d}"
    schedule.every().day.at(schedule_time).do(job)
    
    print(f"⏰ Tweet programado para las {schedule_time} UTC diariamente")
    print(f"   Mensaje: {text[:60]}...")
    
    # Keep scheduler running
    while True:
        schedule.run_pending()
        time.sleep(60)

# ====== TWEETS PREDEFINIDOS ======

PRESALE_TWEETS = [
    "🚀 ¡NEXTIA PRESALE LIVE!\n\n✅ Tier 1: $0.005 (-40% descuento)\n✅ 20% APY Staking\n✅ 4 Smart Contracts auditados\n✅ 500 spots disponibles\n\nÚnete: nextia.token/presale\n\n#DeFi #Token #Presale",
    
    "¿Por qué Nextia Token?\n\n1️⃣ Utilidad REAL (no vaporware)\n2️⃣ Revenue compartido con holders\n3️⃣ 20% APY staking sin lock-up\n4️⃣ Governance descentralizado\n5️⃣ Smart contracts 100% auditados\n\nWhitelist: nextia.token/presale 🔗\n\n#DeFi #Crypto",
    
    "Preguntas frecuentes sobre Nextia Token:\n\n❓ ¿Es seguro?\nSí. 16/16 tests passing. Código en GitHub.\n\n❓ ¿Cuándo mainnet?\nQ1 2026 después de auditoría externa.\n\n❓ ¿Puedo hacer stake?\nSí, desde el presale sale. 20% APY.\n\n#FAQ #DeFi",
    
    "Nextia Trading Bot en vivo 🤖\n\n50+ usuarios activos generando signals\nSeñales automáticas en Telegram\nMachine learning optimization\n\n¡Próximamente integrado en DApp!\n\nSigue: @NextiaToken\n\n#TradingBot #Crypto #Signals",
]

STAKING_TWEETS = [
    "Staking 101 con Nextia 📊\n\n✅ Sin lock-up\n✅ Claim rewards cuando quieras\n✅ 20% APY sostenible\n✅ Calculada por segundo\n✅ Basada en ingresos reales\n\nNo es un ponzi. Es capitalismo. 💰\n\n#DeFi #Staking #Crypto",
    
    "¿Cómo los yields son sostenibles?\n\nNextia Marketing genera ingresos REALES de clientes.\nEsos ingresos se reparten:\n- 50% a stakers (rewards)\n- 25% a desarrollo\n- 25% a operaciones\n\nTransparencia total en DAO governance.\n\n#DeFi #Transparency",
]

COMMUNITY_TWEETS = [
    "¡Únete a nuestra comunidad! 🌍\n\n💬 Telegram: t.me/nextiatokenoficial\n💎 Discord: discord.gg/nextia\n📂 GitHub: github.com/NextiaLabs\n📧 Email: nextiacorp33@gmail.com\n\nVamos a construir esto juntos.\n\n#Community #DeFi #NextiaToken",
]

# ====== MAIN ======

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatización de Twitter para Nextia Token")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--tweet", help="Publicar un tweet individual")
    group.add_argument("--thread", help="Publicar un thread desde archivo (1 tweet por línea)")
    group.add_argument("--presale", action="store_true", help="Publicar tweets de presale")
    group.add_argument("--staking", action="store_true", help="Publicar tweets de staking")
    group.add_argument("--community", action="store_true", help="Publicar tweets de comunidad")
    group.add_argument("--schedule", nargs=2, metavar=("TIME", "TEXT"), help="Agendar tweet para hora específica (HH:MM)")
    
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
                print("❌ El archivo está vacío")
        except FileNotFoundError:
            print(f"❌ Archivo no encontrado: {args.thread}")
    
    elif args.presale:
        print("📢 Publicando tweets de presale...\n")
        for tweet in PRESALE_TWEETS:
            post_single_tweet(tweet)
            time.sleep(3)
    
    elif args.staking:
        print("📊 Publicando tweets de staking...\n")
        for tweet in STAKING_TWEETS:
            post_single_tweet(tweet)
            time.sleep(3)
    
    elif args.community:
        print("🌍 Publicando tweets de comunidad...\n")
        for tweet in COMMUNITY_TWEETS:
            post_single_tweet(tweet)
            time.sleep(3)
    
    elif args.schedule:
        time_str, text = args.schedule
        try:
            hour, minute = map(int, time_str.split(':'))
            post_scheduled(hour, minute, text)
        except ValueError:
            print("❌ Formato de hora inválido. Usa HH:MM (ej: 09:00)")
    
    else:
        print("❌ Por favor especifica --tweet, --thread, --presale, --staking, --community, o --schedule")
        parser.print_help()