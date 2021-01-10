"""
4.4.1節のコードの説明
"""
import dataclasses
import uuid
from typing import Final, NamedTuple

# リスト4.9
@dataclasses.dataclass
class User():
    """
    Userクラスの定義

    Attributes:
        id (UserId): ユーザid
        name (UserName): ユーザ名
    """
    # 本のGuid.NewGuid().ToString()でユニークなIDを取得している
    # pythonならuuidモジュールを使えばよい
    id: Final[UserId] = dataclasses.field(default=uuid.uuid1(), init=False)
    name: Final[UserName]

# リスト4.10
class UserId(NamedTuple):
    """
    ユーザidを表すクラス

    Attributes:
        value (str): ユーザid
    """
    value: str

class UserName:
    """
    ユーザ名を表すクラス

    Attributes:
        value (str): ユーザ名
    """
    def __init__(self, value: str):
        len(value) < 3: raise ValueError("ユーザ名は3文字以上です")
        self.value: Final[str] = value