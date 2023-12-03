from datetime import datetime
from currencies import Currency

from server.src.classes.event.EventABC import EventABC


class ExpenseEvent(EventABC):
    _currency: Currency
    _description: str | None

    def __init__(self, date: datetime.date, amount: float, currency: Currency = Currency('EUR'), description: str = None):
        super().__init__(date, amount)
        self._currency = currency
        self._description = description

    def get_date(self) -> datetime.date:
        return self._date

    def get_value(self) -> float:
        return self._value

    def get_currency(self) -> Currency:
        return self._currency

    def get_description(self) -> str | None:
        return self._description

    def get_amount_with_currency_format(self) -> str:
        return self.get_currency().get_money_with_currency_format(self.get_amount())
    
    def set_date(self, date: datetime.date):
        self._date = date
        
    def set_value(self, value: float):
        self._value = value

    def set_currency(self, currency: Currency):
        self._currency = currency

    def set_description(self, description: str):
        self._description = description

    # Function Aliases
    get_amount = get_value
    set_amount = set_value
