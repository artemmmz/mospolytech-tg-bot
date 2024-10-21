"""Module with enum classes."""

from enum import StrEnum


class Weekday(StrEnum):
    """Enum class of weekdays."""

    MONDAY = '1'
    TUESDAY = '2'
    WEDNESDAY = '3'
    THURSDAY = '4'
    FRIDAY = '5'
    SATURDAY = '6'

    @property
    def previous(self):
        """
        Get the previous day of the week.

        :return: Weekday enum or None.
        """
        members = list(self.__class__)
        current_index = members.index(self)
        if current_index > 0:
            return members[current_index - 1]
        return None

    @property
    def next(self):
        """
        Get the next member of the week.

        :return: Weekday enum.
        """
        members = list(self.__class__)
        current_index = members.index(self)
        if current_index < len(members) - 1:
            return members[current_index + 1]
        return None
