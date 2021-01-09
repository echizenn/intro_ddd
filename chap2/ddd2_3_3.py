"""
2.3節のコードの説明
"""
from dataclasses import dataclass
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

    @property
    def value(self) -> str:
        """
        外部からvalueを取得できるようにする

        Args: None

        Returns:
            str: 名前
        """
        return self._value


# リスト2.26
@dataclass
class FullName:
    """
    リスト2.25のNameクラスを利用したFullNameクラス

    Attributes:
        _first_name (Name): 名
        _last_name (Name): 姓
    """
    _first_name: Final[Name]
    _last_name: Final[Name]

    @property
    def first_name(self) -> Name:
        """
        外部からfirst_nameを取得できるようにする

        Args: None

        Returns:
            Name: 名
        """
        return self._first_name

    @property
    def last_name(self) -> Name:
        """
        外部からlast_nameを取得できるようにする

        Args: None

        Returns:
            Name: 姓
        """
        return self._last_name
