from aiogram import Router
from aiogram.filters import CommandObject
from aiogram.types import Message

from app.filters.commands import Commands

router = Router()


@router.message(Commands.SCHEDULE)
async def command_schedule(message: Message, command: CommandObject) -> None:
    await message.answer('Введите номер группы')


@router.callback_query()
async def callback_schedule():
    ...
