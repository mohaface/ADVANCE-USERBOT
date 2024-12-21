import json
import aiohttp
from aiohttp import ClientSession

class AioHttp:
    @staticmethod
    async def get_json(link):
        async with ClientSession(trust_env=True) as session:
            async with session.get(link) as resp:
                return await resp.json()

    @staticmethod
    async def get_text(link):
        async with ClientSession(trust_env=True) as session:
            async with session.get(link) as resp:
                return await resp.text()

    @staticmethod
    async def get_json_from_text(link):
        async with ClientSession(trust_env=True) as session:
            async with session.get(link) as resp:
                text = await resp.text()
                return json.loads(text)

    @staticmethod
    async def get_raw(link):
        async with ClientSession(trust_env=True) as session:
            async with session.get(link) as resp:
                return await resp.read()

    @staticmethod
    async def get_url(link):
        async with ClientSession(trust_env=True) as session:
            async with session.get(link) as resp:
                return resp.url
