from services.sms.base_sms_gateway import ISmsGateway
from config import config


class KavengarSmsGateway(ISmsGateway):
    def __init__(self):
        self.api_key: config.kavengar_api_key
        self.api_url: config.kavengar_api_url

    async def send(self, recipient: str, body: str, **extra) -> bool:
        return True
