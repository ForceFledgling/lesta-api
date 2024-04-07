import os
import sys
import json
from importlib import import_module
import requests
import datetime

from app.core.exceptions import UnicornException
from app.middlewares import measure_time, measure_time_async
from app.settings import settings
from app.services.api import LestaAPI

from app.api.endpoints import wotb


class CustomService:
    def __init__(self, request):
        self.request = request
        self.params = dict(request.query_params)

    def get_activity(self):
        response = {}

        clan_id = str(self.params["clan_id"])
        clan_info = LestaAPI(
            self.request,
            custom_prefix="/wotb/clans/info/"
        ).run()
        print('clan_info', clan_info)
        response["tag"] = clan_info["data"][clan_id]["tag"]
        response["name"] = clan_info["data"][clan_id]["name"]
        response["members_count"] = clan_info["data"][clan_id]["members_count"]
        
        members_ids = clan_info["data"][self.params["clan_id"]]["members_ids"]
        members_ids_row = ', '.join(map(str, members_ids))
        members_info = LestaAPI(
            self.request,
            custom_prefix="/wotb/clans/accountinfo/",
            custom_params={"account_id": members_ids_row}
        ).run()
        personal_members_info = LestaAPI(
            self.request,
            custom_prefix="/wotb/account/info/",
            custom_params={"account_id": members_ids_row}
        ).run()

        members = {}
        for member_id in members_info["data"]:
            members[member_id] = {
                "name": members_info["data"][member_id]["account_name"],
            }
        
        for member_id in personal_members_info["data"]:
            members[member_id]["last_battle_time"] = datetime.datetime.fromtimestamp(
                personal_members_info["data"][str(member_id)]["last_battle_time"]
            ).strftime("%Y-%m-%d %H:%M:%S")
        
        response["members"] = members
        return response

    def get_clan_members(self):
        clan_members = LestaAPI(request=self.request, func=wotb.clans.get_clans_info, custom_params={"clan_id": "604631", "extra": "members", "fields": "members"}).run()
        return clan_members