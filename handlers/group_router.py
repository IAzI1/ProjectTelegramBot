from string import punctuation

from aiogram import types, Router
from filter.chat_types import ChatTypeFilter

group_router = Router()
group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {'кабан', 'хомяк', 'выхухоль'}

def clear_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@group_router.edited_message()
@group_router.message()
async def clear_cmd(message: types.Message):
    if restricted_words.intersection(clear_text(message.text.lower()).split()):
        await message.answer(f'{message.from_user.first_name} соблюдайте правила группы!')
        await message.delete()