from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.filters.callback_datas import Schedule

HELP_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='📅 Расписание',
                callback_data=Schedule().pack()
            )
        ]
    ]
)
