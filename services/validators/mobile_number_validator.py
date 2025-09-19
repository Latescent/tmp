import re
from lib.translation_manager import tm


def validate_mobile_number(value: str) -> str:
    pattern = r"^(09\d{9}|(\+98|98)9\d{9}|9\d{9})$"
    if not re.match(pattern, value):
        raise ValueError(
            tm(key='invalid-mobile-number')
        )
    return value
