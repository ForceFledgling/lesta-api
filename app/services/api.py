import os
import sys
import json
from importlib import import_module
import requests

from app.core.exceptions import UnicornException
from app.middlewares import measure_time, measure_time_async
from app.settings import settings


class ApiService:
    base_url = "https://papi.tanksblitz.ru"

    def __init__(self, request, custom_prefix=None, custom_params=None):
        self.url = self.base_url + custom_prefix if custom_prefix else self.base_url + request.url.path
        self.params = custom_params or dict(request.query_params)
        if "application_id" not in self.params.keys():
            self.params['application_id'] = settings.application_id

    def run(self):
        try:
            response = requests.post(self.url, params=self.params)
            response.raise_for_status()  # Вызываем исключение когда плохой статус код
            return response.json()
        except requests.RequestException as e:
            raise UnicornException(f"Error during POST request: {e}")
