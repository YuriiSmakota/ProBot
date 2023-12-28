from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultArticle, Message, InputTextMessageContent

router = Router()


@router.inline_query(F.query == "invite")
async def invite_query(message: Message, inline_query: InlineQuery):

    await inline_query.answer(results=[
        InlineQueryResultArticle(
            id=f"{message.from_user.id}",
            title="Title",
            description="Description",
            input_message_content=InputTextMessageContent(message_text="Message Text"),
            thumbnail_url=""

        )
    ], is_personal=True)
