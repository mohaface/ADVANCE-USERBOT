import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Rocky"])

async def join(client):
    try:
        await client.join_chat("SOFIA_TG_BOTS")
    except BaseException:
        pass
