from domain.models.file_relation import FileRelation as DomainFileRelation
from infrastructure.mappers.auto_mapper import AutoMapper
from infrastructure.models.file_relation import FileRelation as OrmFileRelation


class FileRelationMapper(AutoMapper):
    domain_class = DomainFileRelation
    orm_class = OrmFileRelation
    exclude_to_domain = {"created_at", "updated_at", "id"}
