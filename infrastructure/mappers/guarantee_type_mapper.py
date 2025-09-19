from domain.models.guarantee_type import GuaranteeType as DomainGuaranteeType
from infrastructure.models.guarantee_type import GuaranteeType as OrmGuaranteeType
from infrastructure.mappers.auto_mapper import AutoMapper


class GuaranteeTypeMapper(AutoMapper):
    domain_class = DomainGuaranteeType
    orm_class = OrmGuaranteeType
    exclude_to_domain = {"created_at", "updated_at"}