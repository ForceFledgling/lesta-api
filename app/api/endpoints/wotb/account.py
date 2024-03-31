import json

from typing import Annotated
from fastapi import Body

from fastapi import Request, APIRouter
from fastapi import Depends

from app.core.exceptions import UnicornException
from app.models.wotb import accounts
from app.services.api import ApiService


router = APIRouter()


@router.post(
    "/list/",
    description="Получение списка всех аккаунтов по имени."
)
def get_accounts_list(
    request: Request,
    request_data: accounts.PlayersModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


@router.post(
    "/info/",
    description="Получение персональных данных игроков по account_id."
)
def get_accounts_personal_info(
    request: Request,
    request_data: accounts.PlayersPersonalDataModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


