from pydantic import BaseModel, field_validator
from services.validators.mobile_number_validator import validate_mobile_number


class SendOtpCommand(BaseModel):
    mobile: str

    @field_validator("mobile")
    @classmethod
    def validate_mobile_number(cls, value):
        return validate_mobile_number(value)
