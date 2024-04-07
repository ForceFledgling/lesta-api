from fastapi import APIRouter

from app.api.endpoints.wotb import router as wotb_router


def get_path(func):
    path = router.url_path_for(func.__name__)
    return path


router = APIRouter()

router.include_router(wotb_router, prefix='/wotb', tags=['wotb'],)
