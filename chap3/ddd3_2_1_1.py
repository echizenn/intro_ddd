"""
3.2.1節のコードの説明
"""
import dataclasses
from typing import Final

# リスト3.1


@dataclasses.dataclass(frozen=True)
class User:
    """
    ユーザを表すクラス

    Attributes:
        _name (str): ユーザ名

    Raises:
        ArgumentException: ユーザ名が3文字未満のとき
    """
    _name: Final[str]

    def __post_init__(self):
        if len(self._name) < 3: raise ArgumentException("ユーザ名は3文字以上です。", str(self._name))
