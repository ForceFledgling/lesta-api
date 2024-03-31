from pydantic import BaseModel, Field
from typing import Optional, List, Union
from fastapi import Query

from app.models import FieldDescriptions


class CustomClansModel(BaseModel):
    application_id: Optional[str] = Field(Query(
            default=None,
            description=FieldDescriptions.application_id
    ))
    clan_id: Union[int, list] = Field(Query(
        default=604631,
        description=\
            """
        Идентификатор клана.
        Максимальное ограничение: 100.
        Минимальное значение: 1.
            """,
    ))