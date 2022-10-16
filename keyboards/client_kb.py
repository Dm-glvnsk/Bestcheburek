from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('Контактная информация')
b2 = KeyboardButton('Оставить отзыв')
b3 = KeyboardButton('Забронировать стол')
b4 = KeyboardButton('Заказать навынос')
b5 = KeyboardButton('Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)
kb_client.row(b4,b3).row(b5,b2).add(b1)

get_contact_button = KeyboardButton('Оставить контакт')
cancel_button = KeyboardButton('Не оставлю')
main_menu_button = KeyboardButton('Главное меню')

kb_client_review = ReplyKeyboardMarkup(resize_keyboard = True)
kb_client_review.row(get_contact_button, cancel_button).add(main_menu_button)
