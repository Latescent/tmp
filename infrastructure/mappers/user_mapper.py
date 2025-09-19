from domain.models.user import User as DomainUser
from domain.value_objects.mobile_number import MobileNumber
from infrastructure.models.user import User as OrmUser
from infrastructure.mappers.auto_mapper import AutoMapper


class UserMapper(AutoMapper):
    domain_class = DomainUser
    orm_class = OrmUser
    exclude_to_domain = {"created_at", "updated_at"}
    custom_to_domain = {"mobile": lambda val: MobileNumber(val)}
    custom_to_orm = {"mobile": lambda mob: str(mob)}
