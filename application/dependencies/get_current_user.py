from typing import Union
from domain.models.user import User
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from shared.exceptions import UnauthorizedError
from shared.helpers import generate_token_hash
from shared.unit_of_work import get_unit_of_work

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
        token: str = Depends(oauth2_scheme),
        uow: Depends = Depends(get_unit_of_work)
) -> Union[User, None]:
    token_hash = generate_token_hash(token)
    async with uow:
        user = await uow.user_repo.get_by_token(token_hash)
        if not user:
            raise UnauthorizedError()
        return user


async def get_current_admin(
        token: str = Depends(oauth2_scheme),
        uow: Depends = Depends(get_unit_of_work)
) -> Union[User, None]:
    token_hash = generate_token_hash(token)
    async with uow:
        user = await uow.user_repo.get_by_token(token_hash)
        if not user or not user.is_admin:
            raise UnauthorizedError()
        return user
