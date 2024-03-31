import json

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .api import router
from .core.exceptions import UnicornException
from .settings import settings


tags_metadata = [
    {
        'name': 'wotb',
        'description': 'https://developers.lesta.ru/reference/all/wotb/',
    },
]

app = FastAPI(
    title='Неофициальное API для Lesta Games',
    description='https://github.com/ForceFledgling/lesta-api',
    version='0.0.1',
    openapi_tags=tags_metadata,
    docs_url="/docs",
    redoc_url=None,
)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=200,
        content={
            request.state.address: {
                "lesta-api": {
                    "result": "ERROR",
                    "msg": exc.msg
                }
            }
        }
    )
