import json

from typing import Annotated
from fastapi import Body

from fastapi import Request, APIRouter
from fastapi import Depends

from app.core.exceptions import UnicornException
from app.models.wotb import accounts
from app.services.api import ApiService


router = APIRouter()
