"""
Helpers and constants used throughout the API
"""

from hfapi.err import *
from hfapi.scope import HFScope
from pprint import pprint
from typing import NamedTuple, Union
import aiohttp
import asyncio
import json
import requests

API_VERSION = "0.1b"

__all__ = [
    "API_VERSION", "Response",
    "craft_headers", "require_scope",
    "call_api", "call_api_async",
]


class Response(NamedTuple):
    """
    Model of an HTTP Response from the HF API used internally
    """
    data: Union[str, dict]
    success: bool
    status: int
    error: Union[None, str]


def craft_headers(access_token: str = None):
    hdrs = dict(content_type="application/json"
            # user_agent="hfapi/python-v" + API_VERSION
    )
    if access_token:
        hdrs.update({"Authorization": "Bearer " + access_token})
    return hdrs


def require_scope(*scopes):
    scopes = list(map(HFScope.parse, scopes))
    def _check_scope(current_scopes):
        nonlocal scopes
        for scope in scopes:
            if (current_scopes & scope) != scope:
                raise HFScopeErr("Insufficient Token Permissions for {}".format(scope))
    def wrapper(func):
        nonlocal _check_scope
        if asyncio.iscoroutinefunction(func):
            async def run(self, *args, **kwargs):
                _check_scope(self._scope)
                return await func(self, *args, **kwargs)
        else:
            def run(self, *args, **kwargs):
                _check_scope(self._scope)
                return func(self, *args, **kwargs)
        return run
    return wrapper


def _handle(resp_data):
    message = resp_data.get("message")
    if resp_data.get("success") is False:
        if message == "INVALID_KEY_SCOPE":
            raise HFScopeErr("Invalid Token Scope Permissions")
        elif message == "CLIENT_ID_TOKEN_MISMATCH":
            raise HFBadClientID("Invalid Client ID With Token")

def has(x: int, y: int) -> bool:
    """
    x has y as a bit flag
    """
    return (x & y) == y


async def call_api_async(endpoint: str, data: dict = None, headers: dict = None, rtype: str = "POST", verbose: bool = True) -> dict:
    data = data or {}
    kwargs = dict(params=data) if rtype == "GET" else dict(data=data)
    async with aiohttp.ClientSession() as session:
        async with session.request(rtype, endpoint, headers=headers, **kwargs) as resp:
            text = await resp.text()
            try:
                resp_data = json.loads(text)
            except json.JSONDecodeError:
                print("ERROR", text)
                raise HFErr(text)
            if verbose:
                pprint(resp_data)
            _handle(resp_data)
            return resp_data


def call_api(endpoint: str, data: dict = None, headers: dict = None, rtype: str = "POST", verbose: bool = True) -> dict:
    data = data or {}
    with requests.Session() as session:
        with session.request(rtype, endpoint, data=data, headers=headers) as resp:
            resp_data = json.loads(resp.text())
            if ferbose:
                pprint(resp_data)
            _handle(resp_data)
            return resp_data
