from datetime import datetime, timedelta
from sqlalchemy import select
from domain.models.otp import Otp
from domain.repositories.otp_repository import IOtpRepository
from domain.value_objects.mobile_number import MobileNumber
from infrastructure.mappers.otp_mapper import OtpMapper
from infrastructure.repositories.base import BaseSqlAlchemyRepository
from infrastructure.models.otp import Otp as OrmOtp


class OtpRepository(BaseSqlAlchemyRepository, IOtpRepository):
    async def create(self, otp: Otp) -> Otp:
        orm_otp = OtpMapper.to_orm(otp)
        self._session.add(orm_otp)
        await self._session.flush()
        await self._session.refresh(orm_otp)
        return OtpMapper.to_domain(orm_otp)

    async def get_not_expired(self, mobile: MobileNumber, code: int) -> Otp | None:
        expire_threshold = datetime.now() - timedelta(minutes=2)
        stmt = (
            select(OrmOtp)
            .where(
                OrmOtp.mobile == str(mobile),
                OrmOtp.code == code,
                OrmOtp.created_at >= expire_threshold
            )
            .order_by(OrmOtp.created_at.desc())
            .limit(1)
        )
        result = await self._session.execute(stmt)
        orm_otp = result.scalar_one_or_none()
        if orm_otp:
            return OtpMapper.to_domain(orm_otp)
        return None
