"""
Helpers and constants used throughout the API
"""

from typing import NamedTuple, Union
import aiohttp
import requests

API_VERSION = "0.1b"


__all__ = [
    "API_VERSION", "Response",
    "craft_headers", "call_api", "call_api_async",
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
    hdrs = dict(user_agent="hfapi/python v" + API_VERSION)
    if access_token:
        hdrs.update({"Authorization": "Bearer " + access_token})
    return hdrs


async def call_api_async(endpoint: str, data: dict = None, headers: dict = None, rtype: str = "POST"):
    data = data or {}
    async with aiohttp.ClientSession() as session:
        async with session.request(rtype, endpoint, headers=headers, data=data) as resp:
            try:
                resp_data = await resp.json()
                from pprint import pprint
                pprint(resp_data)
                if resp_data.get("success") is False:
                    return Response(resp_data, False, resp.status, resp_data.get("message", ""))
                return Response(resp_data, True, resp.status, None)
            except aiohttp.ContentTypeError:
                print(resp.headers)
                resp_data = await resp.text()
                print("NOT JSON", resp_data)
                return Response(None, False, resp.status, resp_data)
            except Exception as e:
                import traceback
                traceback.print_exc()
                print("Exception in call_api_async", e)
                return Response(None, False, resp.status, str(type(e)))


def call_api(endpoint: str, data: dict = None, headers: dict = None, rtype: str = "POST"):
    data = data or {}
    with requests.Session() as session:
        with session.request(rtype, endpoint, data=data, headers=headers) as resp:
            try:
                resp_data = resp.json()
                if resp_data.get("success") is False:
                    return Response(resp_data, False, resp.status_code, resp_data.get("message", ""))
                return Response(resp_data, True, resp.status_code, None)
            except Exception as e:
                import traceback
                traceback.print_exc()
                print("Exception in `call_api`:", e)
                return Response(None, False, resp.status, str(type(e)))
