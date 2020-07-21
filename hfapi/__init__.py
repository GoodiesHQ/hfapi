"""
HackForums API by Goodies
"""

from .hf_base import HFAppBase, HFClientBase
# from .hf_sync import HFApp, HFClient
from .hf_async import HFAppAsync, HFClientAsync
from . import (
    asks, helpers, scope,
)


from .scope import HFPerms
from .helpers import API_VERSION as __version__
__author__ = "Goodies <goodies@protonmail.com>"


__all__ = [
    "HFClientBase", "HFAppBase",
    "HFAppAsync", "HFClientAsync",
    "HFPerms",
    "asks",
    "helpers",
    "__version__",
]
