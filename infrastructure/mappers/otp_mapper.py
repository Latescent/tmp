from domain.models.otp import Otp as DomainOtp
from domain.value_objects.mobile_number import MobileNumber
from infrastructure.models.otp import Otp as OrmOtp
from infrastructure.mappers.auto_mapper import AutoMapper


class OtpMapper(AutoMapper):
    domain_class = DomainOtp
    orm_class = OrmOtp
    exclude_to_domain = {"id", "created_at", "updated_at"}
    custom_to_domain = {"mobile": lambda val: MobileNumber(val)}
    custom_to_orm = {"mobile": lambda mob: str(mob)}
