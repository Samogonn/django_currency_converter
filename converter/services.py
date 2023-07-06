import currencyapicom
from config import settings


def convert_currencies(amount: float, from_currency: str, to_currency: str) -> float:
    """Функция для расчета стоимости валюты"""

    client = currencyapicom.Client(settings.CURRENCYAPICOM_KEY)
    rates_data = client.latest(from_currency, [to_currency])

    result = rates_data["data"][to_currency]["value"] * amount

    return result
