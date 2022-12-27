from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token='5611740291:AAFrvlpoKSw4PnCzXdkzMGqA4uOP3WQyu78')
dp = Dispatcher(bot)

# ===== Код выполняемый при старте бота =====
async def on_startup(_):
    print('Мы онлайн')

# =====      Обработка команд бота      =====
@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вы зашли в пиццерию "Пицман и Калачев".\nДобро пожаловать!')

@dp.message_handler()
async def command_rejim_rabot(message : types.Message):
    if message.text == 'Режим работы':
        await bot.send_message(message.from_user.id, 'Прием заявок осуществляется ежедневно с 9:00 до 21:00')
    elif message.text == 'Помощь':
        await bot.send_message(message.from_user.id,'Данный телеграм бот предназначен для заказа вкусняшек ;) \n\n Автор: Алексей Дубовцев')

# Эхо ответ
@dp.message_handler()
async def echo_send(message : types.Message):
    await message.answer(message.text)
    #if message.text == 'Режим работы':
    #    await bot.send_message(message.from_user.id, '2 Прием заявок осуществляется ежедневно с 9:00 до 21:00')


# =====        Запуск самого бота         =====
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)