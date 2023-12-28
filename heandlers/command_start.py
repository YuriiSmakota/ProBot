from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.invite_kb import invite_button

router = Router()


@router.message(CommandStart)
async def start(message: Message):
    await message.answer(f"HELLO <b>{message.from_user.username}</b>!",
                         reply_markup=invite_button)


