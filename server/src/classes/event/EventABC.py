import datetime
from abc import ABC, abstractmethod
from typing import Any


class EventABC(ABC):
    def __init__(self, date: datetime.date, value: Any):
        self.date = date
        self.value = value

    @abstractmethod
    def get_date(self):
        pass

    @abstractmethod
    def get_value(self):
        pass
