import translators as ts
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests


API_TOKEN = '1681979069:AAHvVxlxEY_3iCYb9h1mBIebaoei8KuTRkI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Я маленький ботик и только учусь
    """
    await message.reply("Приветствую\n"
                        "Введи число и узнай интересные факты о нём\n"
                        "Делюсь фактами только о натуральных числах ;-)")

@dp.message_handler()
async def echo(message: types.Message):
    try:
        number = int(message.text)
        if number >= 0:
            urls = []
            urls.append('http://numbersapi.com/{}/math'.format(number))
            urls.append('http://numbersapi.com/{}/trivia'.format(number))

            for each in urls:
                res = requests.get(each).text
                await message.answer(res + '\n' + ts.google(res, to_language='ru'))

        else:
            raise ValueError

    except ValueError:
        await message.answer('Пожалуйста введите натуральное число')

    except Exception:
        await message.answer('Произошла неизвестаная ошибка,\n'
                             'попробуйте позднее')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

