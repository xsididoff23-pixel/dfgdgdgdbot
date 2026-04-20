import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector

TOKEN = "8410870219:AAFT55BS8hGfpV2ZcEc7sixXx7QBOkvUpyM"
PROXY_URL = "socks5://127.0.0.1:10801"  # порт как в 2RayTun

async def test():
    connector = ProxyConnector.from_url(PROXY_URL)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(f"https://api.telegram.org/bot{TOKEN}/getMe") as resp:
            print(await resp.text())

asyncio.run(test())