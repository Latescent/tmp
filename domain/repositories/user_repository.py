from abc import ABC, abstractmethod
from typing import List, Optional, Set
from domain.models.user import User
from domain.value_objects.mobile_number import MobileNumber


class IUserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> None:
        """Add a new user"""
        ...

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        """Fetch a user by its ID"""
        ...

    @abstractmethod
    async def get_by_mobile(self, mobile: MobileNumber) -> Optional[User]:
        """Fetch a user by mobile number"""
        ...

    @abstractmethod
    async def get_by_token(self, token: str) -> Optional[User]:
        """Fetch a user by token"""
        ...

    @abstractmethod
    async def update(self, user: User, fields: Optional[Set[str]] = None) -> None:
        """Update an existing user"""
        ...