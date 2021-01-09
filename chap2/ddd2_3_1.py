"""
2.3節のコードの説明
"""
from dataclasses import dataclass
from typing import Final # 再代入不可能という型ヒント

# リスト2.21
@dataclass
class FullName:
    """
    可能な限り値オブジェクトを適用したFullNameクラス

    Attributes:
        _first_name (FirstName): 名を表すオブジェクト
        _last_name (LastName): 姓を表すオブジェクト
    """
    _first_name: Final[FirstName]
    _last_name: Final[LastName]

# リスト2.22
@dataclass
class FirstName:
    """
    名を表す値オブジェクト

    Attributes:
        _value (str): 名前
    """
    _value: Final[str]

    @property
    def value(self) -> str:
        """
        外部からvalueを取得できるようにする

        Args: None

        Returns:
            str: 名前
        """
        return self._value

# リスト2.23
@dataclass
class LastName:
    """
    姓を表す値オブジェクト

    Attributes:
        _value (str): 姓
    """
    _value: Final[str]

    @property
    def value(self) -> str:
        """
        外部からvalueを取得できるようにする

        Args: None

        Returns:
            str: 姓
        """
        return self._value