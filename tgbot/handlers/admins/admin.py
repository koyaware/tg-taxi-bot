from datetime import datetime

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.config import db, ADMIN_IDS
from tgbot.filters import AdminFilter
from tgbot.misc.commands import Commands
from tgbot.misc.keyboards import mainMenuAdmin, ban_users_inline, mailing_inline, adminMenu


async def admin_start(message: Message):
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name, datetime.now())
        for admin in ADMIN_IDS:
            await message.bot.send_message(admin, f"🆕 Новый пользователь:"
                                                  f"\n\nПользователь: @{message.from_user.username}, <b>{message.from_user.first_name}</b>\n"
                                                  f"[ID:{message.from_user.id}] только что зарегестрировался в боте.")
        await message.bot.send_message(message.from_user.id,
                                       text=f'<b>{message.from_user.first_name}</b>, Добро пожаловать в бот '
                                            f'ТРАНСФЕР-МОСТ.РФ 🚕\nДанный бот создаст заказ на вашу поездку', reply_markup=mainMenuAdmin)
    else:
        await message.bot.send_message(message.from_user.id,
                                       text=f'<b>{message.from_user.first_name}</b>, Добро пожаловать в бот '
                                            f'ТРАНСФЕР-МОСТ.РФ 🚕\nДанный бот создаст заказ на вашу поездку', reply_markup=mainMenuAdmin)


async def admin_menu(message: Message):
    await message.bot.send_message(message.from_user.id,
                                   'Добро пожаловать в админ панель!\n\nДля перехода в главное меню, отправьте боту команду - /start.',
                                   reply_markup=adminMenu)


async def ban_users(message: Message):
    await message.bot.send_message(message.from_user.id, '<b>Меню Блокировки пользователей</b>',
                                   reply_markup=ban_users_inline)


async def mailing_menu(message: Message):
    await message.bot.send_message(message.from_user.id, 'Выберите группу пользователей для рассылки: ',
                                   reply_markup=mailing_inline)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start,
        text=['/start', Commands.come_back.value],
        state="*", is_superuser=True)
    dp.register_message_handler(
        admin_menu, AdminFilter(),
        text=Commands.admin_menu.value,
        state='*'
    )
    dp.register_message_handler(
        ban_users, AdminFilter(),
        text=Commands.ban_users.value,
        state='*'
    )
    dp.register_message_handler(
        mailing_menu, AdminFilter(),
        text=Commands.mailing.value,
        state='*'
    )