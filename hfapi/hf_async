"""
Asynchronous Client implementation
"""

from hfapi import asks
from .hf_base import HFAppBase, HFClientBase
from .helpers import Response, call_api_async, craft_headers
import aiohttp
import json


class HFClientAsync(HFClientBase):
    async def me(self):
        response = await call_api_async(
            endpoint=self.url_read,
            headers=craft_headers(self._access_token),
            data={
                "asks": json.dumps({"me":
                    asks.Me.all().dict()
                })
            })
        pprint(response.data)


class HFAppAsync(HFAppBase):
    async def authorize(self, code: str) -> HFClientAsync:
        resp = await call_api_async(
            endpoint=self.url_auth,
            headers=craft_headers(),
            data={
                "grant_type": "authorization_code",
                "client_id": self._client_id,
                "client_secret": self._secret_key,
                "code": code,
            }
        )
        if not resp.success:
            raise Exception(resp.error)
        return HFClientAsync(resp.data.get("acces_token"))
