from aiogram.types import InlineKeyboardMarkup, Message, ReplyKeyboardMarkup


async def answer_edit_message(
    message: Message,
    text: str,
    is_edit: bool = False,
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup = None,
    **kwargs,
) -> Message | bool:
    if is_edit:
        return await message.edit_text(
            text, reply_markup=reply_markup, **kwargs
        )
    return await message.answer(text, reply_markup=reply_markup, **kwargs)
