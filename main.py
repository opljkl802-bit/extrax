import os
from config import API_ID, API_HASH, BOT_TOKEN, AUTH_USERS
from pyrogram import Client, idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

# Auth Users
AUTH_USERS = [ int(chat) for chat in Config.AUTH_USERS.split(",") if chat != '']

# Prefixes
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")

bot = Client(
    "StarkBot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),   # API_ID must be integer
    api_hash=API_HASH,
    sleep_threshold=20,
    plugins=plugins,
    workers=50
)

async def main():
    await bot.start()
    bot_info = await bot.get_me()
    LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
    await idle()

if __name__ == "__main__":
    asyncio.run(main())   # modern way in Python 3.12+
    LOGGER.info("<---Bot Stopped--->")
