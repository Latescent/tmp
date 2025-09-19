from httpx import AsyncClient

from services.sms.base_sms_gateway import ISmsGateway
from config import config
from shared.http_client import http_client_manager


class KavenegarSmsGateway(ISmsGateway):
    def __init__(self):
        self.api_key: str = config.kavenegar_api_key
        self.api_url: str = config.kavenegar_api_url
        self.sender: str = config.kavenegar_sender
        self.http_client: AsyncClient = http_client_manager.get_client()

    async def send(self, recipient: str, body: str, **extra) -> bool:
        payload = {
            "sender": self.sender,
            "message": body,
            "receptor": recipient,
        }
        url = self.api_url.replace("{API-KEY}", self.api_key)
        try:
            response = await self.http_client.get(url, params=payload)
            response.raise_for_status()
            return True
        except Exception:
            return False
