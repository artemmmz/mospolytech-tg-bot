from datetime import time

from aiogram.filters.callback_data import CallbackData


class ScheduleGroup(CallbackData, prefix='schedule_group'):
    group: str


class ScheduleTime(CallbackData, prefix='schedule_time'):
    hours: int
    minutes: int
