from aiogram import Dispatcher

from .taxi_order import register_taxi_order
from .user import register_user


def register_all_user_handlers(dp: Dispatcher):
    register_user(dp)
    register_taxi_order(dp)