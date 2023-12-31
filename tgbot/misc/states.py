from aiogram.dispatcher.filters.state import StatesGroup, State


class FeedbackState(StatesGroup):
    waiting_for_message = State()
    waiting_for_admin_message = State()


class RatesState(StatesGroup):
    message = State()
    ban_id = State()


class MailingState(StatesGroup):
    send_all = State()
    send_sub = State()
    send_not_sub = State()


class TaxiOrderState(StatesGroup):
    name = State()
    date = State()
    time = State()
    phone = State()
    where_from = State()
    where = State()
    rate = State()
    additional = State()
    amount = State()