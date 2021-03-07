from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from promy_api.infra.env import settings
from promy_api.router import offers

app = FastAPI(title=settings.app_name, version=settings.version)

app.add_middleware(CORSMiddleware, allow_origins=['*'])

app.include_router(offers.router, prefix="/offers", tags=["offers"])


def dev():
    uvicorn.run("promy_api.main:app", host="0.0.0.0", port=8000, reload=True)


def prod():
    uvicorn.run("promy_api.main:app", host="0.0.0.0", port=80)

