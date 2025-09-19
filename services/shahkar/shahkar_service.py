from httpx import AsyncClient
from typing import Dict, Any, Optional
from dataclasses import dataclass

from config import config
from shared.http_client import http_client_manager
from domain.value_objects.mobile_number import MobileNumber


@dataclass
class ShahkarResult:
    success: bool
    is_matched: Optional[bool] = None
    data: Optional[Dict[str, Any]] = None
    error_message: str = ""


class ShahkarService:
    def __init__(self):
        self.business_id: str = config.shahkar_business_id
        self.business_token: str = config.shahkar_business_token
        self.api_url: str = config.shahkar_api_url
        self.http_client: AsyncClient = http_client_manager.get_client()

    async def verify_mobile_owner(self, national_id: str, mobile_number: MobileNumber) -> ShahkarResult:
        payload = {
            "requestContext": {
                "apiInfo": {
                    "businessId": self.business_id,
                    "businessToken": self.business_token
                }
            },
            "nationalId": national_id,
            "mobileNumber": mobile_number.value
        }

        try:
            response = await self.http_client.post(self.api_url, json=payload)
            response.raise_for_status()
            response_data = response.json()

            is_matched = response_data.get("isMatched")

            return ShahkarResult(
                success=True,
                is_matched=is_matched,
                data=response_data
            )
        except Exception as e:
            return ShahkarResult(
                success=False,
                error_message=str(e)
            )