import os
import sys
import json
from importlib import import_module
import requests

from app.core.exceptions import UnicornException
from app.middlewares import measure_time, measure_time_async
from app.settings import settings


class LestaAPI:
    base_url = "https://papi.tanksblitz.ru"

    def __init__(self, request, func, custom_params=None):
        from app.api import get_path
        custom_prefix = get_path(func)

        self.url = self.base_url + custom_prefix if custom_prefix else self.base_url + request.url.path
        self.params = custom_params or dict(request.query_params)
        if "application_id" not in self.params.keys():
            self.params['application_id'] = settings.application_id

    def run(self):
        try:
            response = requests.post(self.url, params=self.params)
            if response.status_code not in [200, 201]:
                raise UnicornException(f"LestaAPI error: {e}")
            response_json = response.json()
            if "error" in response_json.keys():
                raise UnicornException(f'LestaAPI error: {response_json["error"]["message"]}')
            return response_json
        except requests.RequestException as e:
            raise UnicornException(f"Error during POST request: {e}")
