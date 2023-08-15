import json

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.config import connect_to_redis, ADMIN_IDS
from tgbot.filters.is_ban import IsBanFilter
from tgbot.misc.commands import Commands
from tgbot.misc.keyboards import cancel_inline, order_rate_inline, order_additional_inline, order_menu_inline, \
    order_pay_inline, buttons_inline
from tgbot.misc.states import TaxiOrderState


async def taxi_order_name(message: Message):
    await message.bot.send_message(message.from_user.id, 'Ваше имя: \n\n<code>Пример: Александр</code>',
                                   reply_markup=cancel_inline)
    await TaxiOrderState.name.set()


async def taxi_order_date(message: Message, state: FSMContext):
    if isinstance(message.text, str):
        redis_pool = await connect_to_redis()
        order_name = {
            'order_name': message.text,
        }
        order_name_str = json.dumps(order_name)
        await redis_pool.set(name='order_name', value=order_name_str)
        await message.bot.send_message(message.from_user.id, 'Дата поездки: \n\n<code>Пример: 01.01.2023</code>',
                                       reply_markup=cancel_inline)
        await state.finish()
        await TaxiOrderState.date.set()
    else:
        await message.bot.send_message(message.from_user.id, 'Введите вверное значение.')


async def taxi_order_time(message: Message, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_date = {
        'order_date': message.text,
    }
    order_date_str = json.dumps(order_date)
    await redis_pool.set(name='order_date', value=order_date_str)
    await message.bot.send_message(message.from_user.id, 'Время поездки: \n\n<code>Пример: 12:00</code>',
                                   reply_markup=cancel_inline)
    await state.finish()
    await TaxiOrderState.time.set()


async def taxi_order_phone(message: Message, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_time = {
        'order_time': message.text,
    }
    order_time_str = json.dumps(order_time)
    await redis_pool.set(name='order_time', value=order_time_str)
    await message.bot.send_message(message.from_user.id, 'Номер телефона: \n\n<code>Пример: 89991112233</code>',
                                   reply_markup=cancel_inline)
    await state.finish()
    await TaxiOrderState.phone.set()


async def taxi_order_where_from(message: Message, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_phone = {
        'order_phone': message.text,
    }
    order_phone_str = json.dumps(order_phone)
    await redis_pool.set(name='order_phone', value=order_phone_str)
    await message.bot.send_message(message.from_user.id, 'Откуда: \n\n<code>Пример: Ижевск</code>',
                                   reply_markup=cancel_inline)
    await state.finish()
    await TaxiOrderState.where_from.set()


async def taxi_order_where(message: Message, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_where_from = {
        'order_where_from': message.text,
    }
    order_where_from_str = json.dumps(order_where_from)
    await redis_pool.set(name='order_where_from', value=order_where_from_str)
    await message.bot.send_message(message.from_user.id, 'Куда: \n\n<code>Пример: Казань</code>',
                                   reply_markup=cancel_inline)
    await state.finish()
    await TaxiOrderState.where.set()


async def taxi_order_rate(message: Message, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_where = {
        'order_where': message.text,
    }
    order_where_str = json.dumps(order_where)
    await redis_pool.set(name='order_where', value=order_where_str)
    await message.bot.send_message(message.from_user.id, 'Выберите тариф: ',
                                   reply_markup=order_rate_inline)
    await state.finish()
    await TaxiOrderState.rate.set()


async def taxi_order_additional_standard(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_rate = {
        'order_rate': 'Стандарт 22₽',
    }
    order_rate_str = json.dumps(order_rate)
    await redis_pool.set(name='order_rate', value=order_rate_str)
    await call.bot.send_message(call.from_user.id, 'Выберите дополнительные услуги: ',
                                reply_markup=order_additional_inline)
    await state.finish()


async def taxi_order_additional_business(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_rate = {
        'order_rate': 'Бизнес 27₽',
    }
    order_rate_str = json.dumps(order_rate)
    await redis_pool.set(name='order_rate', value=order_rate_str)
    await call.bot.send_message(call.from_user.id, 'Выберите дополнительные услуги: ',
                                reply_markup=order_additional_inline)
    await state.finish()


async def taxi_order_additional_station_wagon(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_rate = {
        'order_rate': 'Универсал 28₽',
    }
    order_rate_str = json.dumps(order_rate)
    await redis_pool.set(name='order_rate', value=order_rate_str)
    await call.bot.send_message(call.from_user.id, 'Выберите дополнительные услуги: ',
                                reply_markup=order_additional_inline)
    await state.finish()


async def taxi_order_additional_minivan(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_rate = {
        'order_rate': 'Минивэн 40₽',
    }
    order_rate_str = json.dumps(order_rate)
    await redis_pool.set(name='order_rate', value=order_rate_str)
    await call.bot.send_message(call.from_user.id, 'Выберите дополнительные услуги: ',
                                reply_markup=order_additional_inline)
    await state.finish()


async def taxi_order_amount_missing(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_additional = {
        'order_additional': 'Отсутствует',
    }
    order_additional_str = json.dumps(order_additional)
    await redis_pool.set(name='order_additional', value=order_additional_str)
    await call.bot.send_message(call.from_user.id, 'Выберите способ оплаты: ',
                                reply_markup=order_pay_inline)
    await state.finish()


async def taxi_order_amount_empty(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_additional = {
        'order_additional': 'Пустой багажник',
    }
    order_additional_str = json.dumps(order_additional)
    await redis_pool.set(name='order_additional', value=order_additional_str)
    await call.bot.send_message(call.from_user.id, 'Выберите способ оплаты: ',
                                reply_markup=order_pay_inline)
    await state.finish()


async def taxi_order_amount_child_seat(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_additional = {
        'order_additional': 'Детское кресло + 150₽',
    }
    order_additional_str = json.dumps(order_additional)
    await redis_pool.set(name='order_additional', value=order_additional_str)
    await call.bot.send_message(call.from_user.id, 'Выберите способ оплаты: ',
                                reply_markup=order_pay_inline)
    await state.finish()


async def taxi_order_pay_cash(message: Message, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_pay = {
        'order_pay': 'Наличными 💵',
    }
    order_pay_str = json.dumps(order_pay)
    await redis_pool.set(name='order_pay', value=order_pay_str)
    await message.bot.send_message(message.from_user.id, 'Количество пассажиров: ',
                                   reply_markup=buttons_inline)
    await state.finish()


async def taxi_order_pay_card(message: Message, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_pay = {
        'order_pay': 'Переводом 💳',
    }
    order_pay_str = json.dumps(order_pay)
    await redis_pool.set(name='order_pay', value=order_pay_str)
    await message.bot.send_message(message.from_user.id, 'Количество пассажиров: ',
                                   reply_markup=buttons_inline)
    await state.finish()


async def taxi_order_pay_bill(message: Message, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_pay = {
        'order_pay': 'Расчётный счёт 🧾',
    }
    order_pay_str = json.dumps(order_pay)
    await redis_pool.set(name='order_pay', value=order_pay_str)
    await message.bot.send_message(message.from_user.id, 'Количество пассажиров: ',
                                   reply_markup=buttons_inline)
    await state.finish()


async def taxi_order_list(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    button_number = call.data.split("_")[1]
    order_passengers = {
        'order_passengers': button_number,
    }
    order_passengers_str = json.dumps(order_passengers)
    await redis_pool.set(name='order_passengers', value=order_passengers_str)
    await call.bot.answer_callback_query(call.id, f"Вы выбрали {button_number}.")
    order_name_str = await redis_pool.get('order_name')
    order_name = json.loads(order_name_str)
    name = order_name['order_name']
    order_date_str = await redis_pool.get('order_date')
    order_date = json.loads(order_date_str)
    date = order_date['order_date']
    order_time_str = await redis_pool.get('order_time')
    order_time = json.loads(order_time_str)
    time = order_time['order_time']
    order_phone_str = await redis_pool.get('order_phone')
    order_phone = json.loads(order_phone_str)
    phone = order_phone['order_phone']
    order_where_from_str = await redis_pool.get('order_where_from')
    order_where_from = json.loads(order_where_from_str)
    where_from = order_where_from['order_where_from']
    order_where_str = await redis_pool.get('order_where')
    order_where = json.loads(order_where_str)
    where = order_where['order_where']
    order_rate_str = await redis_pool.get('order_rate')
    order_rate = json.loads(order_rate_str)
    rate = order_rate['order_rate']
    order_additional_str = await redis_pool.get('order_additional')
    order_additional = json.loads(order_additional_str)
    additional = order_additional['order_additional']
    order_pay_str = await redis_pool.get('order_pay')
    order_pay = json.loads(order_pay_str)
    pay = order_pay['order_pay']
    order_success = {
        'order_success': f'Данные заявки:'
                         f'\nИмя: <b>{name}</b>'
                         f'\nДата: <b>{date}</b>'
                         f'\nВремя: <b>{time}</b>'
                         f'\nТелефон: <b>{phone}</b>'
                         f'\nОткуда: <b>{where_from}</b>'
                         f'\nКуда: <b>{where}</b>'
                         f'\nТариф: <b>{rate}</b>'
                         f'\nДополнительные услуги: <b>{additional}</b>'
                         f'\nСпособ оплаты: <b>{pay}</b>'
                         f'\nПассажиров: <b>{button_number}</b>',
        'username': call.from_user.username,
        'first_name': call.from_user.first_name,
        'id': call.from_user.id
    }
    order_success_str = json.dumps(order_success)
    await redis_pool.set(name='order_success', value=order_success_str)
    await call.bot.send_message(call.from_user.id, text=order_success['order_success'],
                                reply_markup=order_menu_inline)
    await state.finish()


async def success_order(call: CallbackQuery, state: FSMContext):
    redis_pool = await connect_to_redis()
    order_success_str = await redis_pool.get('order_success')
    order_success = json.loads(order_success_str)
    success = order_success['order_success']
    username = order_success['username']
    first_name = order_success['first_name']
    user_id = order_success['id']
    await call.bot.send_message(user_id, 'Ваш заказ был успешно отправлен!')
    for admin in ADMIN_IDS:
        await call.bot.send_message(admin, f"Поступил новый заказ от:"
                                           f"\n\nПользователь: @{username}, <b>{first_name}</b>\n"
                                           f"[ID:{user_id}]")
        await call.bot.send_message(admin, text=success)
    await call.bot.send_message(chat_id=-1001907711627, text= f"Поступил новый заказ от:"
                                                              f"\n\nПользователь: @{username}, <b>{first_name}</b>\n"
                                                              f"[ID:{user_id}]")
    await call.bot.send_message(chat_id=-1001907711627, text=success)
    await state.finish()


def register_taxi_order(dp: Dispatcher):
    dp.register_message_handler(
        taxi_order_name, text=Commands.taxi_order.value, state="*"
    )
    dp.register_message_handler(
        taxi_order_date, IsBanFilter(),
        state=TaxiOrderState.name
    )
    dp.register_message_handler(
        taxi_order_time, IsBanFilter(),
        state=TaxiOrderState.date
    )
    dp.register_message_handler(
        taxi_order_phone, IsBanFilter(),
        state=TaxiOrderState.time
    )
    dp.register_message_handler(
        taxi_order_where_from, IsBanFilter(),
        state=TaxiOrderState.phone
    )
    dp.register_message_handler(
        taxi_order_where, IsBanFilter(),
        state=TaxiOrderState.where_from
    )
    dp.register_message_handler(
        taxi_order_rate, IsBanFilter(),
        state=TaxiOrderState.where
    )
    dp.register_callback_query_handler(
        taxi_order_additional_standard, IsBanFilter(),
        text='order_standard',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_additional_business, IsBanFilter(),
        text='order_business',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_additional_station_wagon, IsBanFilter(),
        text='order_station_wagon',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_additional_minivan, IsBanFilter(),
        text='order_minivan',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_amount_missing, IsBanFilter(),
        text='order_missing',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_amount_empty, IsBanFilter(),
        text='order_empty',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_amount_child_seat, IsBanFilter(),
        text='order_child_seat',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_pay_cash, IsBanFilter(),
        text='order_pay_cash',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_pay_card, IsBanFilter(),
        text='order_pay_card',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_pay_bill, IsBanFilter(),
        text='order_pay_bill',
        state='*'
    )
    dp.register_callback_query_handler(
        taxi_order_list, IsBanFilter(),
        lambda c: c.data.startswith('button_'),
        state='*'
    )
    dp.register_callback_query_handler(
        success_order, IsBanFilter(),
        text='order_success',
        state='*'
    )
