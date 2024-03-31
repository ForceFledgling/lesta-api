from pydantic import BaseModel, Field
from typing import Optional, List, Union
from fastapi import Query

from app.models import FieldDescriptions


class ClansModel(BaseModel):
    ''' Data model for a device account '''
    application_id: Optional[str] = Field(Query(
            default=None,
            description=FieldDescriptions.application_id
    ))
    fields: Union[str, list] | None = Field(Query(
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
    search: Optional[str] = Field(Query(
        default=None,
        description=\
            """
        Часть названия или тега клана, по которому осуществляется поиск.
        Не может быть меньше 2 символов.
        При поиске по тегу, "[]" - не нужны.
            """,
    ))


class ClansInfoModel(BaseModel):
    ''' Data model for a device account '''
    application_id: Optional[str] = Field(Query(
            default=None,
            description=FieldDescriptions.application_id
    ))
    clan_id: Union[int, list] = Field(Query(
        description=\
            """
        Идентификатор клана.
        Максимальное ограничение: 100.
        Минимальное значение: 1.
            """,
    ))
    extra: Union[str, list] | None = Field(Query(
        default=None,
        description=\
            """
        Список дополнительных полей, которые будут включены в ответ.
        Допустимые значения:
            "members"
            """,
    ))
    fields: Union[str, list] | None = Field(Query(
            default=None,
            description=FieldDescriptions.fields
    ))
    language: Optional[str] = Field(Query(
            default=None,
            description=FieldDescriptions.language
    ))



class ClansAccountInfoModel(BaseModel):
    ''' Data model for a device account '''
    application_id: Optional[str] = Field(Query(
            default=None,
            description=FieldDescriptions.application_id
    ))
    account_id: Union[int, list] = Field(Query(
            default=None,
            description=FieldDescriptions.account_id
    ))
    extra: Union[str, list] | None = Field(Query(
        default=None,
        description=\
            """
        Список дополнительных полей, которые будут включены в ответ.
        Допустимые значения:
            "members"
            """,
    ))
    fields: Union[str, list] | None = Field(Query(
            default=None,
            description=FieldDescriptions.fields
    ))
    language: Optional[str] = Field(Query(
            default=None,
            description=FieldDescriptions.language
    ))