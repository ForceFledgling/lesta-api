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