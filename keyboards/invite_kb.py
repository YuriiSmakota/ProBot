from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


invite_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='INVITE_FRIEND', switch_inline_query='')
        ]
    ]
)