from .base_mapper import BaseMapper


class AutoMapper(BaseMapper):
    domain_class = None
    orm_class = None
    custom_to_domain = {}
    custom_to_orm = {}
    exclude_to_domain = set()
    exclude_to_orm = set()

    @classmethod
    def to_domain(cls, orm_obj):
        return cls.map(
            orm_obj,
            cls.domain_class,
            exclude=cls.exclude_to_domain,
            custom_conversions=cls.custom_to_domain
        )

    @classmethod
    def to_orm(cls, domain_obj):
        return cls.map(
            domain_obj,
            cls.orm_class,
            exclude=cls.exclude_to_orm,
            custom_conversions=cls.custom_to_orm
        )
