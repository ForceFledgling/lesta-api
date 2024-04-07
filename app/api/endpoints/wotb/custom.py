from fastapi import Request, APIRouter
from fastapi import Depends

from app.models.wotb import custom
from app.services.api import LestaAPI

from app.api.endpoints.wotb.clans import get_clans_info

from app.services.custom import CustomService


router = APIRouter()


@router.post(
    "/get_activity/",
    summary="Получение активности по клану",
    description="Получение активности по клану"
)
def get_activity(
    request: Request,
    request_data: custom.CustomClansModel = Depends(),
):
    service = CustomService(request)
    response = service.get_activity()
    return response


@router.post(
    "/get_clan_members/",
    summary="Кастомный запрос",
    description="Тестовый запрос"
)
def get_clan_members(
    request: Request,
    request_data: custom.CustomClansModel = Depends(),
):
    service = CustomService(request)
    response = service.get_clan_members()
    return response