from datetime import datetime, timedelta
import random
from domain.value_objects.mobile_number import MobileNumber


class Otp:
    def __init__(self, mobile: MobileNumber, code: int, expire_at: datetime):
        self.mobile: MobileNumber = mobile
        self.code: int = code
        self.expire_at: datetime = expire_at

    @classmethod
    def create(cls, mobile: str, code: int | None = None, expire_minutes: int = 2) -> 'Otp':
        mobile_vo = MobileNumber(mobile)
        code = code or random.randint(10000, 99999)
        expire_at = datetime.now() + timedelta(minutes=expire_minutes)
        return cls(mobile=mobile_vo, code=code, expire_at=expire_at)
