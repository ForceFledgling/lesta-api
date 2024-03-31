from fastapi import APIRouter

from app.api.endpoints.wotb import router as wotb_router


router = APIRouter()

router.include_router(wotb_router, prefix='/wotb', tags=['wotb'],)
