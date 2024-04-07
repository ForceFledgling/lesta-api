from pydantic import BaseModel, Field
from typing import Optional, List, Union
from fastapi import Query

from app.models import FieldDescriptions


class PlayersModel(BaseModel):
    ''' Data model for a device account '''
    application_id: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.application_id
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
    fields: Union[str, list, None] = Field(Query(
        default=None,
        description=FieldDescriptions.fields
    ))
    language: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.language
    ))
    limit: Optional[int] = Field(Query(
        default=None,
        description=FieldDescriptions.limit
    ))
    type: Optional[str] = Field(Query(
        default=None,
        description=\
            """
        Тип поиска. По умолчанию: "startswith". 
        Допустимые значения:
            "startswith" — Поиск по начальной части имени игрока без учёта регистра.
            Минимальная длина: 3 символа. Максимальная длина: 24 символа. (используется по умолчанию)
            "exact" — Поиск по строгому соответствию имени игрока без учёта регистра.
            Можно перечислить несколько имён для поиска (до 100 значений), разделив их запятыми.
            """,
    ))


class PlayersPersonalDataModel(BaseModel):
    application_id: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.application_id
    ))
    account_id: Union[int, list] = Field(Query(
        description=FieldDescriptions.account_id
    ))
    access_token: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.access_token
    ))
    extra: Union[str, list, None] = Field(Query(
        default=None,
        description=\
            """
        Список дополнительных полей, которые будут включены в ответ. 
        Допустимые значения:
            "private.grouped_contacts"
            "statistics.rating",
            """,
    ))
    fields: Union[str, list, None] = Field(Query(
        default=None,
        description=FieldDescriptions.fields
    ))
    language: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.language
    ))


class PlayersAchievementsModel(BaseModel):
    application_id: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.application_id
    ))
    account_id: Union[int, list] = Field(Query(
        description=FieldDescriptions.account_id
    ))
    fields: Union[str, list, None] = Field(Query(
        default=None,
        description=FieldDescriptions.fields
    ))
    language: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.language
    ))


class PlayersTankStatsModel(BaseModel):
    application_id: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.application_id
    ))
    account_id: Union[int, list] = Field(Query(
        description=FieldDescriptions.account_id
    ))
    tank_id: int = Field(Query(
        description=FieldDescriptions.tank_id
    ))
    fields: Union[str, list, None] = Field(Query(
        default=None,
        description=FieldDescriptions.fields
    ))
    language: Optional[str] = Field(Query(
        default=None,
        description=FieldDescriptions.language
    ))