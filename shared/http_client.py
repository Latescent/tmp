from httpx import AsyncClient, Timeout, Limits, AsyncHTTPTransport
from typing import Optional


class HttpClient:
    client: Optional[AsyncClient] = None
    connection_pool_size = 100

    @classmethod
    def get_client(cls) -> AsyncClient:
        if cls.client is None:
            raise RuntimeError("HTTP Client is not initialized.")
        return cls.client

    @classmethod
    def startup(cls):
        transport = AsyncHTTPTransport(retries=5)
        timeout = Timeout(10.0, connect=5, read=5)
        limits = Limits(
            max_connections=cls.connection_pool_size,
            max_keepalive_connections=20
        )
        cls.client = AsyncClient(
            transport=transport,
            timeout=timeout,
            limits=limits
        )
        print(f"Async HTTP Client initialized with pool size: {cls.connection_pool_size}")

    @classmethod
    async def shutdown(cls):
        if cls.client:
            await cls.client.aclose()
            cls.client = None
            print("Async HTTP Client closed.")


http_client_manager = HttpClient()
