from datetime import datetime
from currencies import Currency

from server.src.classes.event.EventABC import EventABC
from server.src.utilities.decorators import alias


class ExpenseEvent(EventABC):

    def __init__(self, date: datetime.date, amount: float, currency: Currency = Currency('EUR'), description: str = None):
        super().__init__(date, amount)
        self.currency = currency
        self.description = description

    def get_date(self) -> datetime.date:
        return self.date

    @alias('get_amount')
    def get_value(self) -> float:
        return self.value

    def get_currency(self) -> Currency:
        return self.currency

    def get_description(self) -> str | None:
        return self.description

    def get_amount_with_currency_format(self) -> str:
        return self.currency.get_money_with_currency_format(self.value)
