from fastapi import APIRouter

from app.api.endpoints.wotb.account import router as account_router
from app.api.endpoints.wotb.clanmessages import router as clanmessages_router
from app.api.endpoints.wotb.clans import router as clans_router
from app.api.endpoints.wotb.encyclopedia import router as encyclopedia_router
from app.api.endpoints.wotb.tanks import router as tanks_router
from app.api.endpoints.wotb.tournaments import router as tournaments_router

from app.api.endpoints.wotb.custom import router as custom_router


router = APIRouter()

router.include_router(account_router, prefix='/account')
router.include_router(clanmessages_router, prefix='/clanmessages')
router.include_router(clans_router, prefix='/clans')
router.include_router(encyclopedia_router, prefix='/encyclopedia')
router.include_router(tanks_router, prefix='/tanks')
router.include_router(tournaments_router, prefix='/tournaments')

router.include_router(custom_router, prefix='/custom')