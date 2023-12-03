from abc import ABC, abstractmethod

from server.src.classes.event.EventABC import EventABC


class HistoryABC(ABC):
    _events: list[EventABC]

    def __init__(self, events: list[EventABC]):
        self._events = events

    @abstractmethod
    def get_events(self) -> list[EventABC]:
        pass

    @abstractmethod
    def set_events(self, events: list[EventABC]):
        pass
