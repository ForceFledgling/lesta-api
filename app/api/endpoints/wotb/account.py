import json

from typing import Annotated
from fastapi import Body

from fastapi import Request, APIRouter
from fastapi import Depends

from app.core.exceptions import UnicornException
from app.models.wotb import account
from app.services.api import ApiService


router = APIRouter()


@router.post(
    "/list/",
    summary="Игроки",
    description="Метод возвращает часть списка игроков, отфильтрованную по первым символам имени и отсортированную по алфавиту."
)
def get_accounts_list(
    request: Request,
    request_data: account.PlayersModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


@router.post(
    "/info/",
    summary="Персональные данные игрока",
    description="Метод возвращает информацию об игроке."
)
def get_accounts_personal_info(
    request: Request,
    request_data: account.PlayersPersonalDataModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


@router.post(
    "/achievements/",
    summary="Достижения игрока",
    description="Метод возвращает информацию о достижениях игроков."
)
def get_accounts_personal_info(
    request: Request,
    request_data: account.PlayersAchievementsModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


@router.post(
    "/tankstats/",
    summary="Статистика по технике",
    description="Метод возвращает статистику игроков на данной технике."
)
def get_accounts_personal_info(
    request: Request,
    request_data: account.PlayersTankStatsModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


