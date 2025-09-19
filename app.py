from fastapi import FastAPI
from contextlib import asynccontextmanager
from lib.translation_manager import translation_manager
from api import api_router_v1
from config.settings import config
from shared.http_client import http_client_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    http_client_manager.startup()
    translation_manager.load_translations(file="fa.json")
    yield


app = FastAPI(title=config.app_title,
              lifespan=lifespan,
              docs_url="/api/docs",
              openapi_url="/api/openapi.json",
              redoc_url="/api/redoc")
app.include_router(api_router_v1, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
