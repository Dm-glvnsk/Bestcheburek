from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '5668495266:AAFOZZBmuDKBK23pazejvW2wPXIDLzsqmfw'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage = storage)