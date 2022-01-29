"""
3.5節のコードの説明
"""
import dataclasses
from typing import Final

# リスト3.8
@dataclasses.dataclass
class User:
    """
    無口なコード
    ここでの目的上説明用のdocsはこれ以上書きません

    Note:
        ユーザ名が文字列ということしかわからない
    """
    name: str

# リスト3.9
@dataclasses.dataclass(frozen=True)
class UserName:
    """
    饒舌なコード

    Attributes:
        _value (str): ユーザ名

    Raises:
        ArgumentException: ユーザ名が3文字未満のとき

    Note:
        ユーザ名が3文字以上でなければ動作しないことはコードだけ見てもわかる
    """
    _value: Final[str]

    def __post_init__(self):
        if len(self._value) < 3: raise ArgumentException("ユーザ名は3文字以上です", str(self._value))