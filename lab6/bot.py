import logging 
from aiogram import Bot, Dispatcher, types 
from aiogram.dispatcher.filters import Command, Text 
from aiogram.utils import executor 
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 
# Set up logging 
logging.basicConfig(level=logging.INFO) 
# Initialize bot and dispatcher 
bot = Bot(token='7846199737:AAH_YvNX7YItsV5Mc18JK5Wv_5edSFgjbeY') 
storage = MemoryStorage() 
dp = Dispatcher(bot, storage) 
masters={ 
    "Парикмахер": "Запись на услугу парикмахера", 
    "Мастер маникюра": "Запись на услугу мастра маникюра", 
    "Бровист": "Запись на услугу бровиста", 
    "Косметолог": "Запись на услугу косметолога" 
} 

@dp.message_handler(Command("start")) 
async def start(message: types.Message): 
    await message.answer('Привет! Я бот салона красоты. Какие услуги вас интересуют?') 
    keyboard = InlineKeyboardMarkup() 
    for master in masters.keys(): 
        keyboard.add(InlineKeyboardButton(master, callback_data=master)) 
    await message.answer("Выберите мастера:", reply_markup=keyboard) 

@dp.callback_query_handler(lambda c: c.data in masters.keys()) 
async def process_callback(callback_query: CallbackQuery): 
    master_name = callback_query.data 
    await bot.send_message(callback_query.from_user.id, masters[master_name]) 
    await callback_query.answer() 

if __name__ == '__main__': 
    executor.start_polling(dp, skip_updates=True)
