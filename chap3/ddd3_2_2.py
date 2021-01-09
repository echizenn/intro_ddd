"""
3.2.2節のコードの説明
"""
from dataclasses import dataclass
from typing import Final

# リスト3.4
@dataclass(eq=True)
class UserId():
    """
    識別子とそれを利用したユーザのオブジェクト

    Attributes:
        _value (str): ユーザ識別子

    Note:
        dataclass(eq=True)で比較可能な状態にしている
        なんでreadonlyでないのかはよくわからない
    """
    _value: str

class User:
    """
    識別子を利用したユーザのオブジェクト

    Attributes:
        _id: ユーザ識別子オブジェクト
        _name: ユーザ名
    """
    _id: Final[UserId]
    _name: str