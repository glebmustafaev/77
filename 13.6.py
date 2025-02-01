from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать',callback_data='calories')
button2 = InlineKeyboardButton(text='Информация',callback_data='info')
kb.add(button1)
kb.add(button2)

@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Рады вас видеть',reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb)

@dp.callback_query_handler(text='info')
async def infor(call):
    await call.message.answer('Я -- бот, рассчитывающий норму ккал по упрощенной формуле Миффлина-Сан Жеора.')
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    try:
        age = float(data['age'])
        weight = float(data['weight'])
        growth = float(data['growth'])
    except:
        await message.answer(f'Не могу конвертировать введенные значения в числа.')
        await state.finish()
        return

    # Упрощенный вариант формулы Миффлина-Сан Жеора:
    # для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5
    calories_man = 10 * weight + 6.25 * growth - 5 * age + 5
    #для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161
    calories_wom = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Норма (муж.): {calories_man} ккал')
    await message.answer(f'Норма (жен.): {calories_wom} ккал')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
