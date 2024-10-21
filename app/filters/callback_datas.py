from aiogram.filters.callback_data import CallbackData

from app.utils.enums import Weekday


class Schedule(CallbackData, prefix='schedule'): ...


class ScheduleGroup(Schedule, prefix='schedule_group'):
    group: str


class ScheduleWeekday(ScheduleGroup, prefix='schedule_weekday'):
    weekday: Weekday


class ScheduleDate(ScheduleGroup, prefix='schedule_date'):
    date: str


class ScheduleWeek(ScheduleGroup, prefix='schedule_week'):
    year: int
    week: int


class ScheduleDateWeek(ScheduleGroup, prefix='schedule_date_week'):
    year: int
    week: int
