"""
Define the asks that are used within the HF API

These are used with boolean values internally for queries
as well as responses from the server
"""

from pydantic import BaseModel
from typing import Optional, List, Union


class HFAsk(BaseModel):
    """
    Base class for all HF Asks
    """


class Authorize(HFAsk):
    state: Optional[str]    # Optional state
    code: str               # Code


class Post(HFAsk):
    """
    Create a post on an existing thread
    """
    tid: str                # Target thread ID
    message: str            # Message contents


class Thread(HFAsk):
    """
    Create a thread on a subforum
    """
    fid: str                # Target forum ID
    subject: str            # Thread subject
    message: str            # Thread contents


class Bytes(HFAsk):
    """
    Transfer bytes between users
    """
    uid: str                # Target user ID
    amount: int             # Amount of bytes to transfer
    reason: Optional[str]   # Transfer reason


class Deposit(HFAsk):
    """
    Deposit bytes
    """
    deposit: int            # Deposit amount


class Withdraw(HFAsk):
    """
    Withdraw bytes
    """
    withdraw: int           # Withdrawal amount


class Me(HFAsk):
    vault: Union[str, bool]
    uid: Union[str, bool]
    username: Union[str, bool]
    usergroup: Union[str, bool]
    displaygroup: Union[str, bool]
    additionalgroups: Union[str, bool]
    postnum: Union[int, bool]
    awards: Union[str, bool]
    bytes: Union[int, bool]
    threadnum: Union[int, bool]
    avatar: Union[str, bool]
    avatardimensions: Union[str, bool]
    lastvisit: Union[str, bool]
    usertitle: Union[str, bool]
    website: Union[str, bool]
    timeonline: Union[str, bool]
    reputation: Union[str, bool]
    referrals: Union[str, bool]
    lastactive: Union[str, bool]
    unreadpms: Union[str, bool]
    invisible: Union[str, bool]
    totalpms: Union[str, bool]

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
