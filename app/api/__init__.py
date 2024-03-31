# from fastapi import APIRouter
from app.core.router import CustomAPIRouter

from app.api.endpoints.wotb import router as wotb_router


# router = APIRouter()
router = CustomAPIRouter()

router.include_router(wotb_router, prefix='/wotb', tags=['wotb'],)
