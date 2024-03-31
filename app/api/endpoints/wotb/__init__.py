from fastapi import APIRouter

from app.api.endpoints.wotb.account import router as account_router


router = APIRouter()

router.include_router(account_router, prefix='/account')
