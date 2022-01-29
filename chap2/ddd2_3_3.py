"""
2.3節のコードの説明
"""
import dataclasses
import re
from typing import Final

# リスト2.25
@dataclasses.dataclass(frozen=True)
class Name:
    """
    名前を表現するクラス

    Attributes:
        _value (str): 名前、アルファベットのみで構成される

    Raises:
        ArgumentException: アルファベット以外が名前として使われているとき
    """
    _value: Final[str]

    def __post_init__(self):
        if not re.fullmatch('[a-zA-Z]+', self._value):
            raise ArgumentException("許可されていない文字が使われています。", str(self._value))


# リスト2.26
@dataclasses.dataclass(frozen=True)
class FullName:
    """
    リスト2.25のNameクラスを利用したFullNameクラス

    Attributes:
        _first_name (Name): 名
        _last_name (Name): 姓
    """
    _first_name: Final[Name]
    _last_name: Final[Name]

