from pathlib import Path

from aiogram.contrib.fsm_storage.redis import RedisStorage2
from environs import Env
from redis import asyncio as aioredis

from tgbot.db import Database

BASE_DIR = (Path(__file__).resolve()).parent


env = Env()
env.read_env('.env')

BOT_TOKEN = env.str('BOT_TOKEN')

ADMIN_IDS = [2420239, 627071371, ]


db = Database('database.db')
storage = RedisStorage2(host='localhost', port=6379, db=0)


async def connect_to_redis():
    redis_pool = await aioredis.from_url('redis://localhost')
    return redis_pool
