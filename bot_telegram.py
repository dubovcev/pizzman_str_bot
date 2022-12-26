from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token='5611740291:AAFrvlpoKSw4PnCzXdkzMGqA4uOP3WQyu78')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вы зашли в пиццерию "Пицман и Калачев".\nДобро пожаловать!')
        await message.delete
    except:
        await message.reply('Общение с ботом только через личные сообщения, напишите ему:\nhttps://t.me/pizzman_str_bot')

@dp.message_handler(commands=['Режим_работы'])
async def command_rejim_rabot(message : types.Message):
    await bot.send_message(message.from_user.id, 'Прием заявок осуществляется ежедневно с 9:00 до 21:00')

@dp.message_handler()
async def echo_send(message : types.Message):
    await message.answer(message.text)



executor.start_polling(dp, skip_updates=True)