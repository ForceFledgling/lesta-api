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
    # print('path1', request.url.path)
    service = CustomService(request) # закомментил чтобы не вызывалось
    response = service.run()
    return response


# @router.post(
#     "/test2/",
#     summary="Кастомный запрос2",
#     description="Тестовый запрос2",
# )
# def test2(
#     request: Request,
#     request_data: custom.CustomClansModel = Depends(),
# ):
    
#     test(request, request_data)  # хочу вызвать другой эндпоинт "test"
    
#     print('path2', request.url.path)
#     return {}
