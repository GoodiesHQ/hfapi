"""
Asynchronous Client implementation
"""

from typing import Union
from hfapi import asks
from hfapi.scope import HFScope
from .hf_base import HFAppBase, HFClientBase
from .helpers import Response, call_api_async, craft_headers, require_scope, has
import aiohttp
import json


class HFClientAsync(HFClientBase):
    @require_scope("POSTSWRITE")
    async def make_post(self, thread: Union[str, asks.Thread], message: str):
        return asks.Post.load(
            await call_api_async(
                endpoint=self.url_write,
                headers=craft_headers(self._access_token),
                data=asks.to_data(
                    asks.Post(
                        tid=thread.tid if isinstance(thread, asks.Thread) else thread,
                        message=message,
                    )
                ),
            )
        )

    @require_scope("BASIC")
    async def me(self):
        ask = asks.Me.all()
        if not has(self._scope, HFScope.ADV_R):
            ask.lastactive = None
            ask.unreadpms = None
            ask.invisible = None
            ask.totalpms = None
            ask.warningpoints = None
        return asks.Me.load(
            await call_api_async(
                endpoint=self.url_read,
                headers=craft_headers(self._access_token),
                data=asks.to_data(ask),
            )
        )


class HFAppAsync(HFAppBase):
    async def authorize(self, code: str) -> HFClientAsync:
        data = await call_api_async(
            endpoint=self.url_auth,
            headers=craft_headers(),
            data={
                "grant_type": "authorization_code",
                "client_id": self._client_id,
                "client_secret": self._secret_key,
                "code": code,
            }
        )
        return HFClientAsync(data.get("access_token"), data.get("scope"))
