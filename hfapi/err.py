"""
Exceptions used in HF API
"""

__all__ = [
    "HFErr", "HFScopeErr",
    "HFBadToken", "HFBadClientID", "HFBadSecretKey",
]


class HFErr(Exception):
    """
    Base class for HF Errors
    """


class HFScopeErr(HFErr):
    """
    Insufficient permissions for the requested API
    """


class HFBadToken(HFErr):
    """
    Authentication token is not currently valid
    """


class HFBadClientID(HFErr):
    """
    Invalid Client ID
    """


class HFBadSecretKey(HFErr):
    """
    Invalid Secret Key
    """
