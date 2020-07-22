"""
HackForums API by Goodies
"""

# from .hf_sync import HFApp, HFClient
from .helpers import API_VERSION
from .hf_async import HFAppAsync, HFClientAsync
from .hf_base import HFAppBase, HFClientBase
from .scope import HFScope
from . import (
    asks, helpers, scope,
)

__version__ = API_VERSION
__author__ = "Goodies <goodies@protonmail.com>"

__all__ = [
    "HFClientBase", "HFAppBase",
    "HFAppAsync", "HFClientAsync",
    "HFScope",
    "asks",
    "helpers",
    "scope"
    "__version__", "__author__",
]
