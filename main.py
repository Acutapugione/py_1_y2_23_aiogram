import logging
from aiogram import Bot, Dispatcher, executor, types
import json
# import os


with open('secrets.json') as _:
    # settings = json.loads(_.read())
    settings = json.load(_)
API_TOKEN = settings.get('API_TOKEN')
# API_TOKEN = os.getenv('API_TOKEN')
# print( os.getenv('API_TOKEN') )
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    # keyb = types.ReplyKeyboardMarkup()
    # keyb.add(types.KeyboardButton("Hellooooo"))
    keyb = types.InlineKeyboardMarkup()
    keyb.add(types.InlineKeyboardButton("Секрет", callback_data="secret_token"))
    keyb.add(types.InlineKeyboardButton("Користувачі", callback_data="user_data"))
    await message.reply("Hi!\nI'm Acuta's python bot!\nPowered by aiogram.", reply_markup=keyb)

@dp.message_handler(commands=['users'])
async def get_users(message: types.Message):
    await message.reply([1, 2, 3, 4, 5])
    
    
@dp.callback_query_handler(lambda x: x.data == "user_data")
async def secret_token(callback: types.CallbackQuery):
    obj = {
        'name': 'Dmytro',
        'age': 27,
    }
    await callback.message.reply(obj)
    
    
@dp.callback_query_handler(lambda x: x.data == "secret_token")
async def secret_token(callback: types.CallbackQuery):
    await callback.answer('Secret token passed')
    await callback.message.reply('Secret token passed')
    

    
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(message.text)
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)