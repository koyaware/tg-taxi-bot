from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from tgbot.misc.commands import Commands

btnTaxiOrder = KeyboardButton(Commands.taxi_order.value)
btnOnlineCalculator = KeyboardButton(Commands.online_calculator.value, web_app=WebAppInfo(url='https://xn----7sbp3acjidhfbkt.xn--p1ai/%D0%BF%D1%80%D0%B5%D0%B4%D0%B2%D0%B0%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D1%80%D0%B0%D1%81%D1%87%D0%B5%D1%82-%D1%81%D1%82%D0%BE%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8/#calc'))
btnRates = KeyboardButton(Commands.rates.value)
btnBecomeDriver = KeyboardButton(Commands.become_driver.value)
btnReviews = KeyboardButton(Commands.reviews.value, web_app=WebAppInfo(url='https://xn----7sbp3acjidhfbkt.xn--p1ai/%D0%BE%D1%82%D0%B7%D1%8B%D0%B2%D1%8B/'))
btnFeedback = KeyboardButton(Commands.feedback.value)
btnAdmin = KeyboardButton(Commands.admin_menu.value)
btnBanUsers = KeyboardButton(Commands.ban_users.value)
btnSpeaker = KeyboardButton(Commands.mailing.value)
btnComeBack = KeyboardButton(Commands.come_back.value)

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenuAdmin = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnTaxiOrder)
mainMenu.add(btnOnlineCalculator)
mainMenu.add(btnRates, btnReviews)
mainMenu.add(btnBecomeDriver)
mainMenu.add(btnFeedback)

mainMenuAdmin.add(btnTaxiOrder)
mainMenuAdmin.add(btnOnlineCalculator)
mainMenuAdmin.add(btnRates, btnReviews)
mainMenuAdmin.add(btnBecomeDriver)
mainMenuAdmin.add(btnFeedback)
mainMenuAdmin.add(btnAdmin)

adminMenu = ReplyKeyboardMarkup(resize_keyboard=True)
adminMenu.add(btnBanUsers, btnSpeaker)
adminMenu.add(btnComeBack)

become_driver_inline = InlineKeyboardMarkup(row_width=1)
become_driver_inline.add(InlineKeyboardButton(text='♦️Стать водителем ♦️', url='https://t.me/transfermostbot'))


cancel_inline = InlineKeyboardMarkup()

btnCancel = InlineKeyboardButton(text='❌ Отмена', callback_data='cancelbutton')

cancel_inline.insert(btnCancel)

feedback_inline = InlineKeyboardMarkup(row_width=1)

btnBanInline = InlineKeyboardButton(text="🚫 Забанить пользователя", callback_data='ban_user')
btnFeedbackInline = InlineKeyboardButton(text="📨 Ответить", callback_data='feedback_user')

feedback_inline.insert(btnFeedbackInline)
feedback_inline.insert(btnBanInline)

ban_users_inline = InlineKeyboardMarkup(row_width=1)

btnBanIDInline = InlineKeyboardButton(text="🚫 Забанить пользователя", callback_data='ban_user_id')
btnUnBanInline = InlineKeyboardButton(text="🔥 Разбанить пользователя", callback_data='unban_user')
btnUserBannedInline = InlineKeyboardButton(text="📋 Таблица заблокированных", callback_data='banned_user')

ban_users_inline.insert(btnBanIDInline)
ban_users_inline.insert(btnUnBanInline)
ban_users_inline.insert(btnUserBannedInline)

mailing_inline = InlineKeyboardMarkup(row_width=1)

btnSendAll = InlineKeyboardButton(text="📟 Отправить всем пользователям", callback_data='send_all')

mailing_inline.insert(btnSendAll)

order_rate_inline = InlineKeyboardMarkup(row_width=1)

btnStandard = InlineKeyboardButton(text='Стандарт 22₽', callback_data='order_standard')
btnBusiness = InlineKeyboardButton(text='Бизнес 27₽', callback_data='order_business')
btnStationWagon = InlineKeyboardButton(text='Универсал 28₽', callback_data='order_station_wagon')
btnMinivan = InlineKeyboardButton(text='Минивэн 40₽', callback_data='order_minivan')

order_rate_inline.insert(btnStandard)
order_rate_inline.insert(btnBusiness)
order_rate_inline.insert(btnStationWagon)
order_rate_inline.insert(btnMinivan)

order_additional_inline = InlineKeyboardMarkup(row_width=1)

btnMissing = InlineKeyboardButton(text='Отсутствует', callback_data='order_missing')
btnEmpty = InlineKeyboardButton(text='Пустой багажник', callback_data='order_empty')
btnChildSeat = InlineKeyboardButton(text='Детское кресло + 150₽', callback_data='order_child_seat')

order_additional_inline.insert(btnMissing)
order_additional_inline.insert(btnEmpty)
order_additional_inline.insert(btnChildSeat)

order_pay_inline = InlineKeyboardMarkup(row_width=1)

btnCash = InlineKeyboardButton(text='Наличными 💵', callback_data='order_pay_cash')
btnCard = InlineKeyboardButton(text='Переводом 💳', callback_data='order_pay_card')
btnBill = InlineKeyboardButton(text='По расчётному счёту +10%🧾', callback_data='order_pay_bill')

order_pay_inline.insert(btnCash)
order_pay_inline.insert(btnCard)
order_pay_inline.insert(btnBill)

order_menu_inline = InlineKeyboardMarkup(row_width=1)

btnSuccess = InlineKeyboardButton(text='✅ Подтвердить', callback_data='order_success')

order_menu_inline.insert(btnSuccess)
order_menu_inline.insert(btnCancel)

buttons = [
    InlineKeyboardButton(f"{i}", callback_data=f"button_{i}") for i in range(1, 9)
]
buttons_inline = InlineKeyboardMarkup(row_width=4)

for i in range(0, len(buttons), 4):
    buttons_inline.add(*buttons[i:i + 4])

