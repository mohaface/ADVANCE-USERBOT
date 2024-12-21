import json
import aiohttp
import ssl
from aiohttp import ClientSession, TCPConnector

class AioHttp:
    @staticmethod
    async def get_json(link):
        connector = TCPConnector(ssl=False)
        async with ClientSession(connector=connector) as session:
            async with session.get(link) as resp:
                return await resp.json()

    @staticmethod
    async def get_text(link):
        connector = TCPConnector(ssl=False)
        async with ClientSession(connector=connector) as session:
            async with session.get(link) as resp:
                return await resp.text()

    @staticmethod
    async def get_json_from_text(link):
        connector = TCPConnector(ssl=False)
        async with ClientSession(connector=connector) as session:
            async with session.get(link) as resp:
                text = await resp.text()
                return json.loads(text)

    @staticmethod
    async def get_raw(link):
        connector = TCPConnector(ssl=False)
        async with ClientSession(connector=connector) as session:
            async with session.get(link) as resp:
                return await resp.read()

    @staticmethod
    async def get_url(link):
        connector = TCPConnector(ssl=False)
        async with ClientSession(connector=connector) as session:
            async with session.get(link) as resp:
                return resp.url
