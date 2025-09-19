import re
from lib.translation_manager import tm


class MobileNumber:
    __MOBILE_PATTERN = re.compile(r"^(09\d{9}|(\+98|98)9\d{9}|9\d{9})$")

    def __init__(self, value: str):
        normalized = self._normalize(value)
        if not self.__MOBILE_PATTERN.match(normalized):
            raise ValueError(tm(key='invalid-mobile-number'))
        self._value = normalized

    @staticmethod
    def _normalize(mobile_number: str) -> str:
        return mobile_number[-10:]

    @property
    def value(self) -> str:
        return f"0{self._value}"

    def __str__(self):
        return self._value

    def __eq__(self, other):
        if isinstance(other, MobileNumber):
            return self._value == other._value
        if isinstance(other, str):
            return self._value == MobileNumber(other)._value
        return False
