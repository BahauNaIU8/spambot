import asyncio
import threading

from telethon import TelegramClient
from config import API_ID, API_HASH




client = TelegramClient('session_name2', API_ID, API_HASH)

client.start()

client.disconnect()