from fastapi import Request, APIRouter
from fastapi import Depends

from app.models.wotb import custom
from app.services.api import ApiService

from app.api.endpoints.wotb.clans import get_clans_info


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
    custom_prefix = "/wotb/account/list/"
    service = ApiService(request, custom_prefix)
    response = service.run()
    print('request custom', request.url)
    return response