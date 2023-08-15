from datetime import datetime

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.config import db, ADMIN_IDS
from tgbot.filters.is_ban import IsBanFilter
from tgbot.misc.commands import Commands
from tgbot.misc.keyboards import mainMenu, cancel_inline, become_driver_inline
from tgbot.misc.states import FeedbackState


async def user_start(message: Message):
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name, datetime.now())
        for admin in ADMIN_IDS:
            await message.bot.send_message(admin, f"🆕 Новый пользователь:"
                                                  f"\n\nПользователь: @{message.from_user.username}, <b>{message.from_user.first_name}</b>\n"
                                                  f"[ID:{message.from_user.id}] только что зарегестрировался в боте.")
        await message.bot.send_message(message.from_user.id,
                                       text=f'<b>{message.from_user.first_name}</b>, Добро пожаловать в бот '
                                            f'ТРАНСФЕР-МОСТ.РФ 🚕\nДанный бот создаст заказ на вашу поездку',
                                       reply_markup=mainMenu)
    else:
        await message.bot.send_message(message.from_user.id,
                                       text=f'<b>{message.from_user.first_name}</b>, Добро пожаловать в бот '
                                            f'ТРАНСФЕР-МОСТ.РФ 🚕\nДанный бот создаст заказ на вашу поездку',
                                       reply_markup=mainMenu)


async def cancel_button(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.bot.delete_message(call.from_user.id, call.message.message_id)
    await call.bot.send_message(call.from_user.id, "Действие отменено.")


async def rates(message: Message):
    photo_url = 'https://xn----7sbp3acjidhfbkt.xn--p1ai/tarif.jpg'
    await message.bot.send_photo(message.from_user.id, photo=photo_url)


async def become_driver(message: Message):
    text = (
        "Набираем водителей из Ижевска, Казани Уфы, Самары, Перми, Екатеринбурга на подработку в междугороднем "
        "пассажирском такси на личных автомобилях."
        "\nТребования:"
        "\n • ответственность"
        "\n • иномарка либо минимум ЛАДА ВЕСТА"
        "\n • автомобиль, не старше 8 лет"
        "\n • наличие кондиционера"
        "\n • опыт работы в междугородних поездках"
        "\n • проживание в Основных городах где мы работаем"
    )
    await message.bot.send_message(message.from_user.id, text, reply_markup=become_driver_inline)


async def user_feedback(message: Message):
    await message.bot.send_message(message.from_user.id,
                                   "Задайте ваш вопрос текстом, фотографией или любым другим медиавложением: ",
                                   reply_markup=cancel_inline)
    await FeedbackState.waiting_for_message.set()


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_callback_query_handler(
        cancel_button, IsBanFilter(), text="cancelbutton", state='*'
    )
    dp.register_message_handler(
        rates, IsBanFilter(),
        text=Commands.rates.value,
        state='*'
    )
    dp.register_message_handler(
        become_driver, IsBanFilter(),
        text=Commands.become_driver.value,
        state='*'
    )
    dp.register_message_handler(
        user_feedback, IsBanFilter(), text=Commands.feedback.value,
        state="*"
    )