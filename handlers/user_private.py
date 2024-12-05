from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filter.chat_types import ChatTypeFilter
from keyboards.reply import start_kb3, del_keyboard


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f'🟢 Привет {user_name}, виртуальный помощник',
                         reply_markup=start_kb3.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что вас интересует?')
                         )


@user_private_router.message(F.text.lower() == 'меню')
@user_private_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer('🟢 Меню ресторана: ', reply_markup=del_keyboard)


@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def info(message: types.Message):
    await message.answer("🟢 О нас:", reply_markup=del_keyboard)


@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payments'))
async def payments(message: types.Message):
    text = as_marked_section(
        Bold('Варианты оплаты:'),
        'Картой онлайн в боте',
        'При получении доставкой',
        'В заведении наличкой/картой',
        marker='✅ '
    )
    await message.answer(text.as_html(), reply_markup=del_keyboard)


@user_private_router.message(F.text.lower() == 'варианты доставки')
@user_private_router.message(Command('shipping'))
async def shipping(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold('Варианты доставки/заказа:'),
            'Курьер',
            'Самовывоз',
            'Забронировать столик у нас',
            marker='✅ '),
        as_marked_section(
            Bold('Нельзя:'),
            'Почта',
            'Голубь',
            marker='❌ '
        ),
        sep='\n--------------------------------------------\n'
    )
    await message.answer(text.as_html(), reply_markup=del_keyboard)
