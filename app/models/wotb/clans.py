from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import Query

from app.models import field_descriptions


class ClansModel(BaseModel):
    ''' Data model for a device account '''
    application_id: Optional[str] = Field(Query(
        default=None,
        description=field_descriptions["application_id"],
    ))
    search: str = Field(Query(
        description=\
            """
            Строка поиска по имени игрока.
            Вид поиска и минимальная длина строки поиска зависят от параметра type.
            При использовании типа поиска exact можно перечислить несколько имён для поиска, разделив их запятыми.
            Mаксимальная длина: 24.
            """,
    ))
    fields: Optional[str] = Field(Query(
        default=None,
        description=field_descriptions["fields"],
    ))
    language: Optional[str] = Field(Query(
        default="ru",
        description=field_descriptions["language"],
    ))
    limit: Optional[int] = Field(Query(
        default=100,
        description=field_descriptions["limit"],
    ))
    type: Optional[str] = Field(Query(
        default="startswith",
        description=\
            """
            Часть названия или тега клана, по которому осуществляется поиск.
            Не может быть меньше 2 символов.
            """,
    ))