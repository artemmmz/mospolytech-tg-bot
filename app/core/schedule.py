from datetime import date
from typing import Dict, List

from pydantic import BaseModel, Field

from app.utils.enums import Weekday


class Auditory(BaseModel):
    title: str = Field(alias='title')

    @property
    def url(self) -> str | None:
        return None

    @property
    def type(self) -> str:
        return self.title


class Lesson(BaseModel):
    subject: str = Field(alias='sbj')
    teacher: str = Field(alias='teacher')
    auditories: List[Auditory] = Field(alias='auditories')
    date_from: date = Field(alias='df')
    date_to: date = Field(alias='dt')
    dates_str: str = Field(alias='dts')
    type: str = Field(alias='type')
    location: str = Field(alias='location')

    @property
    def auditories_text(self) -> str:
        return ' '.join([auditory.title for auditory in self.auditories])


class Schedule(BaseModel):
    lessons: Dict[Weekday, Dict[str, List[Lesson]]] = Field(alias='grid')
