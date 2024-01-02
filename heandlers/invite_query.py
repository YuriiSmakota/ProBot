from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

router = Router()


@router.inline_query(F.query == "invite")
async def invite_query(inline_query: InlineQuery):
    invite_text = (f"Дорогий друже! З радістю, запрошую тебе "
            f"<a href='https://t.me/mmmgamebot?start='>прийняти участь</a> в <b>ексклюзивній грі</b>.\n"
            f"В якій, завдяки взаємній підтримці та колективним зусиллям, ми прийдемо до спільного успіху.")

    await inline_query.answer(results=[
        InlineQueryResultArticle(
            id=f"1",
            title="Запрошення.",
            description="Нажми на мене, та відправ запрошення своєму другу.",
            input_message_content=InputTextMessageContent(message_text=invite_text),
            thumbnail_url="https://icon-library.com/images/invite-friends-icon/invite-friends-icon-15.jpg"

        )
    ], is_personal=True)
