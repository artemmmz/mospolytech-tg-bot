from aiogram import Router
from aiogram.types import Message

from app.filters.commands import Commands

router = Router()


@router.message(Commands.START)
async def command_start(message: Message):

    await message.answer('Привет! Я - удобный бот, который будет тебе присылать расписание вечером со всей информацией')


@router.message(Commands.HELP)
async def command_help(message: Message):
    await message.answer('Ну тут будет хелп')
