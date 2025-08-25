from typing import Optional
from domain.value_objects.mobile_number import MobileNumber


class User:
    def __init__(self, role_id: int, mobile: MobileNumber, **kwargs) -> None:
        self.id: Optional[int] = kwargs.get('id')
        self.role_id: int = role_id
        self.first_name: Optional[str] = kwargs.get('first_name')
        self.last_name: Optional[str] = kwargs.get('last_name')
        self.mobile: MobileNumber = mobile
        self.national_code: Optional[str] = kwargs.get('national_code')

    @classmethod
    def create(cls, role_id: int, mobile: str, **kwargs):
        mobile_vo = MobileNumber(mobile)
        return cls(role_id=role_id, mobile=mobile_vo, **kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'mobile':
                self.mobile = MobileNumber(value)
            else:
                setattr(self, key, value)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
