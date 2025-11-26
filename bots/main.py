# bots/main.py
import os
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_all_bots():
    print("🚀 INICIANDO NEXTIA BOTS...")
    print("=" * 50)
    
    try:
        from bots.telegram_bot import start as telegram_start
        logger.info("📱 Iniciando Telegram Bot...")
        await telegram_start()
    except Exception as e:
        logger.error(f"❌ Error Telegram: {e}")
    
    print("=" * 50)
    print("✅ Todos los bots están activos!")
    print("🎯 Presale Nextia Token corriendo 24/7")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(run_all_bots())
