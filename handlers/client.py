from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client, kb_client_review
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
#from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте!', reply_markup = kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс. Напишите ему: \nhttps://t.me/bestcheburek_bot')

# Кнопка "Контактная информация"
async def information_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Адрес: Комарово, 2-ая Дачная улица, 3\nРежим работы: 12:00 - 23:00\nТелефон: 8(921)9655544')

# Кнопка "Оставить отзыв"

class FSMClientReview(StatesGroup):
    review = State()
    number = State()



async def review_command(message : types.Message):
    await FSMClientReview.review.set()
    await bot.send_message(message.from_user.id,'Оставьте свой отзыв тут')

# Ловим отзыв
async def get_review(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data['review'] = message.text
    await bot.send_message("-1001762638281", 'Новый отзыв!')
    await bot.send_message("-1001762638281", data['review'])
    await bot.send_message(message.from_user.id, 'Оставите контакт для нашего ответа?', reply_markup=kb_client_review)
    await state.finish()

# Номер телефона
async def get_contact_command(message : types.Message):
    await FSMClientReview.number.set()
    await bot.send_message(message.from_user.id,'Напишите свой номер телефона для связи')

async def get_contact(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
    #await FSMAdmin.next()
    await bot.send_message("-1001762638281", data['number'])
    await state.finish()

# Кнопка "Не оставлять"

async def cancel_button_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы в главном меню', reply_markup = kb_client)

# Кнопка "Главное меню"

async def main_menu_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы в главном меню', reply_markup = kb_client)
# Кнопка "Забронировать стол"

async def book_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 10:00 до 22:00')

# Кнопка "Заказать навынос"

async def order_command(message : types.Message):


# Кнопка "Меню"

async def menu_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 10:00 до 22:00')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands = ['start', 'help'])
    dp.register_message_handler(information_command, lambda message: 'Контактная информация' in message.text)
    dp.register_message_handler(review_command, lambda message: 'Оставить отзыв' in message.text)
    dp.register_message_handler(book_command, lambda message: 'Забронировать стол' in message.text)
    dp.register_message_handler(order_command, lambda message: 'Заказать навынос' in message.text)
    dp.register_message_handler(menu_command, lambda message: 'Меню' in message.text)
    dp.register_message_handler(get_review, state=FSMClientReview.review)
    dp.register_message_handler(get_contact, state=FSMClientReview.number)
    dp.register_message_handler(get_contact_command, lambda message: 'Оставить контакт' in message.text)
    dp.register_message_handler(main_menu_command, lambda message: 'Главное меню' in message.text)
    dp.register_message_handler(cancel_button_command, lambda message: 'Не оставлю' in message.text)