import asyncio
from aiogram import Bot

TOKEN = "8410870219:AAFT55BS8hGfpV2ZcEc7sixXx7QBOkvUpyM"

async def test():
    bot = Bot(token=TOKEN)
    me = await bot.get_me()
    print(f"✅ Бот работает: {me.username}")

asyncio.run(test())