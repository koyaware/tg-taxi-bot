from aiogram import Dispatcher

from tgbot.handlers.admins.admin import register_admin
from tgbot.handlers.admins.ban_users import register_ban_users
from tgbot.handlers.admins.feedback import register_feedback_handlers
from tgbot.handlers.admins.mailing import register_mailings


def register_admin_handlers(dp: Dispatcher):
    register_admin(dp)
    register_feedback_handlers(dp)
    register_ban_users(dp)
    register_mailings(dp)