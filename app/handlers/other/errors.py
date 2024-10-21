import logging

from aiogram import Router
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent

from app.exceptions.api_error import APIError
from app.exceptions.invallid_argument import InvalidArgumentError
from app.exceptions.schedule import ScheduleError
from app.exceptions.too_many_arguments import TooManyArgumentsError

router = Router()


@router.error(ExceptionTypeFilter(APIError))
async def mospolytech_api_error(event: ErrorEvent):
    await event.update.message.answer(
        'Сервер с расписанием не отвечает. Попробуйте позже ⏰🔄\n\n'
    )
    logging.error(f'{event.exception}')


@router.error(ExceptionTypeFilter(InvalidArgumentError))
async def invalid_argument_error(event: ErrorEvent):
    await event.update.message.answer(
        'Вы ввели неправильный аргумент для команды'
    )


@router.error(ExceptionTypeFilter(ScheduleError))
async def schedule_error(event: ErrorEvent):
    exception: ScheduleError = event.exception
    await event.update.message.answer(f'{exception.message}')


@router.error(ExceptionTypeFilter(TooManyArgumentsError))
async def too_many_arguments_error(event: ErrorEvent):
    await event.update.message.answer(f'Слишком много аргументов')


@router.error()
async def other_errors(event: ErrorEvent):
    text = (
        'Упс... Кажется, возникла неизвестная ошибка, '
        'но мы её быстро устраним! 🔧✨'
    )
    if event.update.message:
        await event.update.message.answer(text)
    elif event.update.callback_query:
        await event.update.callback_query.message.answer(text)

    logging.error(
        f'{event.exception.__class__.__name__}: {event.exception} \n'
    )
