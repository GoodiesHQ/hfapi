"""
Define the asks that are used within the HF API

These are used with boolean values internally for queries
as well as responses from the server
"""

from collections import ChainMap
from datetime import datetime as dt
from pydantic import BaseModel
from typing import Optional, List, Union
from abc import ABC, abstractproperty, abstractmethod
import json


class HFAsk(ABC, BaseModel):
    """
    Base class for all HF Asks
    """
    @classmethod
    @abstractmethod
    def name(cls) -> str:
        """
        Name of the ask as it appears on the HF API
        """

    @classmethod
    def load(cls, response):
        """
        Load the object from a servers response
        """
        if cls.name() in response:
            items = response.pop(cls.name())
            if isinstance(items, dict):
                return cls(**items)
            elif isinstance(items, list):
                if len(items) == 1:
                    return cls(**items[0])
                return [cls(**item) for item in items]
            raise NotImplementedError

    def clean(self):
        """
        Return cleaned version of the data
        """
        return {k: v for (k, v) in self.dict().items() if v is not None}

    def data(self):
        name = self.name()
        pfx = "" if name == "me" else "_"
        return {name: {pfx + k: v for k, v in self.clean().items()}}


def to_data(*asks: HFAsk):
    return {"asks": json.dumps(
        dict(ChainMap(*[ask.data() for ask in asks])),
        # separators=(",", ":"),
    )}

class Authorize(HFAsk):
    state: Optional[str]    # Optional state
    code: str               # Code

    def load(self, response):
        raise NotImplementedError


class Post(HFAsk):
    """
    Create a post on an existing thread
    """
    pid: Optional[int] = None
    tid: int
    uid: Optional[int] = None                
    fid: Optional[int] = None
    dateline: Optional[str] = None
    message: Optional[str] = None
    subject: Optional[str] = None
    edituid: Optional[str] = None

    @classmethod
    def name(cls):
        return "posts"

class Thread(HFAsk):
    """
    Create a thread on a subforum
    """
    fid: str                # Target forum ID
    subject: str            # Thread subject
    message: str            # Thread contents

    @property
    def name(self):
        return "threads"


class Bytes(HFAsk):
    """
    Transfer bytes between users
    """
    uid: str                # Target user ID
    amount: int             # Amount of bytes to transfer
    reason: Optional[str]   # Transfer reason

    @property
    def name(self):
        return "bytes"


class Deposit(HFAsk):
    """
    Deposit bytes
    """
    deposit: int            # Deposit amount

    @classmethod
    def name(cls):
        return "deposit"


class Withdraw(HFAsk):
    """
    Withdraw bytes
    """
    withdraw: int           # Withdrawal amount

    @classmethod
    def name(cls):
        return "withdraw"


class Me(HFAsk):
    vault: Union[float, bool] = None
    uid: Union[str, bool] = None
    username: Union[str, bool] = None
    usergroup: Union[str, bool] = None
    displaygroup: Union[str, bool] = None
    additionalgroups: Union[str, bool] = None
    postnum: Union[int, bool] = None
    awards: Union[int, bool] = None
    bytes: Union[float, bool] = None
    threadnum: Union[int, bool] = None
    avatar: Union[str, bool] = None
    avatardimensions: Union[str, bool] = None
    lastvisit: Union[int, bool] = None
    usertitle: Union[str, bool] = None
    website: Union[str, bool] = None
    timeonline: Union[int, bool] = None
    reputation: Union[int, bool] = None
    referrals: Union[int, bool] = None
    lastactive: Union[int, bool] = None
    unreadpms: Union[int, bool] = None
    invisible: Union[int, bool] = None
    totalpms: Union[int, bool] = None
    warningpoints: Union[int, bool] = None

    @classmethod
    def name(cls):
        return "me"

    @staticmethod
    def all():
        return Me(
            vault=True, uid=True, username=True, usergroup=True,
            displaygroup=True, additionalgroups=True, postnum=True,
            awards=True, bytes=True, threadnum=True, avatar=True,
            avatardimensions=True, lastvisit=True, usertitle=True,
            website=True, timeonline=True, reputation=True,
            referrals=True, lastactive=True, unreadpms=True,
            invisible=True, totalpms=True,
        )
