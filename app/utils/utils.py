"""Module with other util functions."""

from app.utils.dicts import WEEKDAYS_VARIABLES
from app.utils.enums import Weekday


def get_weekday_by_word(word: str) -> Weekday | None:
    """
    Get Weekday object by variable of words.

    :param word: Variable of words from WEEKDAYS_VARIABLES.
    :return: Weekday object or None.
    """
    for key, value in WEEKDAYS_VARIABLES.items():
        if word.strip().lower() in value:
            return key
    return None
