from aiogram.types import InlineKeyboardButton


def get_left_arrow(callback_data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text='<-', callback_data=callback_data)


def get_right_arrow(callback_data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text='->', callback_data=callback_data)
