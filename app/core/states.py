from typing import Final

from aiogram.fsm.state import State, StatesGroup


class ScheduleState(StatesGroup):
    GROUP: Final = State()
    TYPE: Final = State()

    WEEKDAY: Final = State()
    DATE: Final = State()


class SubscribeState(StatesGroup):
    GROUP: Final = State()
    TIME: Final = State()
