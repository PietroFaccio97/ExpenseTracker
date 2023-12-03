import datetime
from abc import ABC, abstractmethod
from typing import Any


class EventABC(ABC):
    _date: datetime.date
    _value: Any

    def __init__(self, date: datetime.date, value: Any):
        self._date = date
        self._value = value

    @abstractmethod
    def get_date(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_date(self, date: datetime.date):
        pass

    @abstractmethod
    def set_value(self, value: Any):
        pass
