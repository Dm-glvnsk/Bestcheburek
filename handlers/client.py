from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'У нас есть чебуреки', reply_markup = kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс. Напишите ему: \nhttps://t.me/Yesh_test_bot')

# Кнопка "Контактная информация"
async def information_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Адрес: Комарово, 2-ая Дачная улица, 3\nРежим работы: 12:00 - 23:00\nТелефон: 8(921)9655544')

# Кнопка "Оставить отзыв"

async def review_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 10:00 до 22:00')

# Кнопка "Забронировать стол"

async def book_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 10:00 до 22:00')

# Кнопка "Заказать навынос"

async def order_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 10:00 до 22:00')

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