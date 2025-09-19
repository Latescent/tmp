from domain.models.file import File as DomainFile
from infrastructure.mappers.auto_mapper import AutoMapper
from infrastructure.models.file import File as OrmFile


class FileMapper(AutoMapper):
    domain_class = DomainFile
    orm_class = OrmFile
    exclude_to_domain = {"created_at", "updated_at", "deleted_at"}
