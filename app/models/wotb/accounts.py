from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import Query

class PlayersModel(BaseModel):
    ''' Data model for a device account '''
    application_id: Optional[str] = Field(Query(
        default=None,
        description="Идентификатор приложения. Если не указывать, используется идентификатор данного API.",
    ))
    search: str = Field(Query(
        description="Строка поиска по имени игрока. Вид поиска и минимальная длина строки поиска зависят от параметра type. При использовании типа поиска exact можно перечислить несколько имён для поиска, разделив их запятыми. Mаксимальная длина: 24.",
    ))
    fields: Optional[str] = Field(Query(
        default=None,
        description="Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.",
    ))
    language: Optional[str] = Field(Query(
        default="ru",
        description=\
            """Язык локализации. По умолчанию: "ru". Допустимые значения: "en" — English, "ru" — Русский (используется по умолчанию)"""
    ))
    limit: Optional[int] = Field(Query(
        default=100,
        description="Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в None (по умолчанию).",
    ))
    type: Optional[str] = Field(Query(
        default="startswith",
        description=\
            """Тип поиска. По умолчанию: "startswith". Допустимые значения:
                "startswith" — Поиск по начальной части имени игрока без учёта регистра. Минимальная длина: 3 символа. Максимальная длина: 24 символа. (используется по умолчанию)
                "exact" — Поиск по строгому соответствию имени игрока без учёта регистра. Можно перечислить несколько имён для поиска (до 100 значений), разделив их запятыми.
            """,
    ))


class PlayersPersonalDataModel(BaseModel):
    application_id: Optional[str] = Field(Query(
        default=None,
        description="Идентификатор приложения. Если не указывать, используется идентификатор данного API.",
    ))
    account_id: Optional[int] = Field(Query(
        description="Идентификатор аккаунта игрока. Максимальное ограничение: 100.",
    ))
    access_token: Optional[str] = Field(Query(
        default=None,
        description="Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени.",
    ))
    extra: Optional[str] = Field(Query(
        default=None,
        description=\
            """Список дополнительных полей, которые будут включены в ответ. Допустимые значения:
                "private.grouped_contacts"
                "statistics.rating"",
            """,
    ))
    fields: Optional[str] = Field(Query(
        default=None,
        description="Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.",
    ))
    language: Optional[str] = Field(Query(
        default="ru",
        description=\
            """Язык локализации. По умолчанию: "ru". Допустимые значения: "en" — English, "ru" — Русский (используется по умолчанию)"""
    ))