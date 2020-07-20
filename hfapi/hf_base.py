"""
Base classes for HF App and Client implementations
"""


from abc import ABC, abstractproperty, abstractmethod
from hfapi.auth import HFAuth
from hfapi.asks import HFAsk
from hfapi.helpers import API_VERSION


class HFUrlMixin:
    """
    Mixin providing the URLs associated with the HF API
    """
    @property
    def url_base(self):
        return "https://hackforums.net/api/v2"

    @property
    def url_auth(self):
        return self.url_base + "/authorize"

    def url_auth_page(self, client_id, state: str = None, redirect_uri: str = None):
        return ( self.url_auth
                 + "?response_type=code"
                 + "&client_id=" + client_id
                 + (state and ("&state=" + state) or "")
                 + (redirect_uri and ("&redirect_uri=" + redirect_uri) or ""))

    @property
    def url_read(self):
        return self.url_base + "/read"

    @property
    def url_write(self):
        return {self.url_base} + "/write"


class HFClientBase(ABC, HFUrlMixin):
    def __init__(self, access_token, **kwargs):
        self._access_token = access_token


class HFAppBase(ABC, HFUrlMixin):
    """
    Base class for HF API

    Synchronous and asynchronous implementations will need to implement these accordingly
    """
    def __init__(self, client_id: str, secret_key: str, redirect_uri: str = None):
        self._client_id = client_id
        self._secret_key = secret_key
        self._redirect_uri = redirect_uri
        self._state = None

    @property
    def auth_page(self):
        return self.url_auth_page(self._client_id, redirect_uri=self._redirect_uri)

    @abstractmethod
    def authorize(self, code: str) -> HFClientBase:
        """
        Submit a code to authorize the app for a user
        """
