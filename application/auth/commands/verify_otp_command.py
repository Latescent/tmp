from typing import Optional

from pydantic import BaseModel, field_validator
from services.validators.mobile_number_validator import validate_mobile_number


class VerifyOtpCommand(BaseModel):
    mobile: str
    code: int

    @field_validator("mobile")
    @classmethod
    def validate_mobile_number(cls, value):
        return validate_mobile_number(value)
