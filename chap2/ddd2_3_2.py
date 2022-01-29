"""
2.3節のコードの説明
"""
import dataclasses
import re
from typing import Final

# リスト2.24
@dataclasses.dataclass(frozen=True)
class FullName:
    """
    FullNameでルールを担保する

    Attributes:
        _first_name (str): 名
        _last_name (str): 姓

    Raises:
        ValueRrror: 姓名にアルファベット以外が使われているとき

    Note:
        この状態ではインスタンス同士の比較はできないです。
    """
    _first_name: Final[str]
    _last_name: Final[str]

    def __post_init__(self):
        if not self._validate_name(self.first_name):
            raise ArgumentException("許可されていない文字が使われています。", str(self.first_name))
        if not self._validate_name(self.last_name):
            raise ArgumentException("許可されていない文字が使われています。", str(self.last_name))

    @staticmethod
    def _validate_name(value: str) -> bool:
        # アルファベットに限定する
        return re.fullmatch('[a-zA-Z]+', value)