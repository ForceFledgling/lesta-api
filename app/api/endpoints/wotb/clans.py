import json

from typing import Annotated
from fastapi import Body

from fastapi import Request, APIRouter
from fastapi import Depends

from app.core.exceptions import UnicornException
from app.models.wotb import clans
from app.services.api import ApiService


router = APIRouter()


@router.post(
    "/list/",
    summary="Кланы",
    description="Метод проводит поиск по кланам и сортирует их в указанном порядке."
)
def get_clans_list(
    request: Request,
    request_data: clans.ClansModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


@router.post(
    "/info/",
    summary="Данные клана",
    description="Метод возвращает полную информацию о клане."
)
def get_clans_info(
    request: Request,
    request_data: clans.ClansInfoModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


@router.post(
    "/accountinfo/",
    summary="Данные клана",
    description=\
        """
        Метод возвращает клановые данные игрока.
        Клановые данные игрока существуют только для аккаунтов, которые принимали участие в деятельности клана:
            рассылали запросы на вступление, были игроками клана и т.д.
        """
)
def get_clans_accountinfo(
    request: Request,
    request_data: clans.ClansAccountInfoModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response


@router.post(
    "/glossary/",
    summary="Глоссарий кланов",
    description=\
        """
        Метод возвращает информацию о клановых сущностях.
        """
)
def get_clans_glossary(
    request: Request,
    request_data: clans.ClansGlossaryModel = Depends(),
):
    service = ApiService(request)
    response = service.run()
    return response
