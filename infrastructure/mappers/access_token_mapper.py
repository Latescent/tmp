from domain.models.access_token import AccessToken as DomainAccessToken
from infrastructure.models.access_token import AccessToken as OrmAccessToken
from infrastructure.mappers.auto_mapper import AutoMapper


class AccessTokenMapper(AutoMapper):
    domain_class = DomainAccessToken
    orm_class = OrmAccessToken
    exclude_to_domain = {"id", "created_at", "updated_at"}
    exclude_to_orm = {"plain_text_token"}
