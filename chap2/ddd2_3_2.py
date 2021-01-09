"""
2.3節のコードの説明
"""
import re
from typing import Final

# リスト2.24
class FullName:
    """
    FullNameでルールを担保する

    Attributes:
        _first_name (str): 名
        _last_name (str): 姓

    Raises:
        ValueRrror: 姓名にアルファベット以外が使われているとき
    """
    def __init__(self, first_name: str, last_name: str):
        if not self._validate_name(first_name):
            raise ValueError("許可されていない文字が使われています")
        if not self._validate_name(last_name):
            raise ValueError("許可されていない文字が使われています")

        self._first_name: Final[str] = first_name
        self._last_name: Final[str] = last_name

    @staticmethod
    def _validate_name(value: str) -> bool:
        # アルファベットに限定する
        return re.fullmatch('[a-zA-Z]+', value)

    @property
    def first_name(self) -> str:
        """
        外部からfirst_nameを取得できるようにする

        Args: None

        Returns:
            str: 名
        """
        return self._first_name

    @property
    def last_name(self) -> str:
        """
        外部からlast_nameを取得できるようにする

        Args: None

        Returns:
            str: 姓
        """
        return self._last_name