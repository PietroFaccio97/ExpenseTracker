from server.src.classes.event.EventABC import EventABC
from server.src.classes.event.implementations.ExpenseEvent import ExpenseEvent
from server.src.classes.history.HistoryABC import HistoryABC
from server.src.classes.statistics.implementations.ExpenseStatistics import ExpenseStatistics


class ExpenseHistory(HistoryABC):
    _statistics: ExpenseStatistics

    def __init__(self, events: list[ExpenseEvent]):
        super().__init__(events)

    def get_events(self) -> list[EventABC]:
        return self._events

    def set_events(self, events: list[EventABC]):
        self._events = events
