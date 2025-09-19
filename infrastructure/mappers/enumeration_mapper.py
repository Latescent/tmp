from domain.models.enumeration import Enumeration as DomainEnumeration
from infrastructure.models.enumeration import Enumeration as OrmEnumeration
from infrastructure.mappers.auto_mapper import AutoMapper


class EnumerationMapper(AutoMapper):
    domain_class = DomainEnumeration
    orm_class = OrmEnumeration
    exclude_to_domain = {"created_at", "updated_at"}