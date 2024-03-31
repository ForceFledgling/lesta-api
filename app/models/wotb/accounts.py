from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import Query

from app.models import field_descriptions


class PlayersModel(BaseModel):
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
        default=None,
        description=field_descriptions["limit"],
    ))
    type: Optional[str] = Field(Query(
        default="startswith",
        description=\
            """
            Тип поиска. По умолчанию: "startswith". Допустимые значения:
            "startswith" — Поиск по начальной части имени игрока без учёта регистра. Минимальная длина: 3 символа. Максимальная длина: 24 символа. (используется по умолчанию)
            "exact" — Поиск по строгому соответствию имени игрока без учёта регистра. Можно перечислить несколько имён для поиска (до 100 значений), разделив их запятыми.
            """,
    ))


class PlayersPersonalDataModel(BaseModel):
    application_id: Optional[str] = Field(Query(
        default=None,
        description=field_descriptions["application_id"],
    ))
    account_id: Optional[int] = Field(Query(
        description=\
            """
            Идентификатор аккаунта игрока.
            Максимальное ограничение: 100.
            """,
    ))
    access_token: Optional[str] = Field(Query(
        default=None,
        description=field_descriptions["access_token"],
    ))
    extra: Optional[str] = Field(Query(
        default=None,
        description=\
            """
            Список дополнительных полей, которые будут включены в ответ. 
            Допустимые значения:
                "private.grouped_contacts"
                "statistics.rating",
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