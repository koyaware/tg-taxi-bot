from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from tgbot.config import db
from tgbot.filters import AdminFilter
from tgbot.misc.keyboards import cancel_inline
from tgbot.misc.states import MailingState


async def send_all_users(call: CallbackQuery):
    await call.bot.send_message(call.from_user.id, 'Введите сообщение для всех пользователей: ', reply_markup=cancel_inline)
    await MailingState.send_all.set()


async def send_all_users_state(message: Message, state: FSMContext):
    users = db.get_users()
    for user in users:
        await message.bot.copy_message(user, message.chat.id, message.message_id)
    await message.bot.send_message(message.from_user.id, 'Сообщение было отправлено.')
    await state.finish()


def register_mailings(dp: Dispatcher):
    dp.register_callback_query_handler(
        send_all_users, AdminFilter(),
        text='send_all',
        state='*'
    )
    dp.register_message_handler(
        send_all_users_state, AdminFilter(),
        state=MailingState.send_all,
        content_types=["text", "sticker", "pinned_message", "photo", "audio", "document", "animation ", "video",
                       "voice", "has_media_spoiler", "contact", "location"]
    )