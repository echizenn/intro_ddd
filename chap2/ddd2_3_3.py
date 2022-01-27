"""
2.3節のコードの説明
"""
import dataclasses
import re
from typing import Final

# リスト2.25
class Name:
    """
    名前を表現するクラス

    Attributes:
        _value (str): 名前、アルファベットのみで構成される

    Raises:
        ValueError: アルファベット以外が名前として使われているとき
    """
    def __init__(self, value: str):
        if not value: raise ValueError("valueが定義されていません")
        if not re.fullmatch('[a-zA-Z]+', value):
            raise ValueError("許可されていない文字が使われています")
        
        self._value: Final[str] = value


# リスト2.26
@dataclass(frozen=True)
class FullName:
    """
    リスト2.25のNameクラスを利用したFullNameクラス

    Attributes:
        _first_name (Name): 名
        _last_name (Name): 姓
    """
    _first_name: Final[Name]
    _last_name: Final[Name]

