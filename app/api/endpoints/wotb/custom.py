from fastapi import Request, APIRouter
from fastapi import Depends

from app.models.wotb import custom
from app.services.api import ApiService

from app.api.endpoints.wotb.clans import get_clans_info

from app.services.custom import CustomService


router = APIRouter()


@router.post(
    "/test/",
    summary="Кастомный запрос",
    description="Тестовый запрос"
)
def test(
    request: Request,
    request_data: custom.CustomClansModel = Depends(),
):
    service = CustomService(request)
    response = service.run()
    return response