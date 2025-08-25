from services.sms.base_sms_gateway import ISmsGateway


class FakeSmsGateway(ISmsGateway):
    def __init__(self):
        ...

    async def send(self, recipient: str, body: str, **extra) -> bool:
        return True
