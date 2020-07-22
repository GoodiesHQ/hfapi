from enum import IntFlag, auto
from typing import Union


"""

BASICWRITE ADVWRITE POSTSWRITE USERS BYTESWRITE CONTRACTSWRITE

"""


class HFScope(IntFlag):
    """
    Permissions
    """
    BASIC_R = auto()
    BASIC_W = auto()
    ADV_R = auto()
    ADV_W = auto()
    POSTS_R = auto()
    POSTS_W = auto()
    USERS = auto()
    BYTES_R = auto()
    BYTES_W = auto()
    CONTRACTS_R = auto()
    CONTRACTS_W = auto()

    @staticmethod
    def parse(scope: Union[str, int]):
        if isinstance(scope, (HFScope, int)):
            return scope
        val = 0
        for part in scope.split():
            val |= {
                "BASIC": HFScope.BASIC_R,
                "BASICWRITE": HFScope.BASIC_R | HFScope.BASIC_W,
                "ADV": HFScope.ADV_R,
                "ADVWRITE": HFScope.ADV_R | HFScope.ADV_W,
                "POSTS": HFScope.POSTS_R,
                "POSTSWRITE": HFScope.POSTS_R | HFScope.POSTS_W,
                "BYTES": HFScope.BYTES_R,
                "BYTESWRITE": HFScope.BYTES_R | HFScope.BYTES_W,
                "CONTRACTS": HFScope.CONTRACTS_R,
                "CONTRACTSWRITE": HFScope.CONTRACTS_R | HFScope.CONTRACTS_W,
            }.get(part, 0)
        return val

