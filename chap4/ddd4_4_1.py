"""
4.4.1節のコードの説明
"""
import dataclasses
import uuid
from typing import Final

# リスト4.10
@dataclasses.dataclass(frozen=True)
class UserId():
    """
    ユーザidを表すクラス

    Attributes:
        value (str): ユーザid
    """
    value: str

@dataclasses.dataclass(frozen=True)
class UserName:
    """
    ユーザ名を表すクラス

    Attributes:
        value (str): ユーザ名

    Raises:
        ArgumentException: ユーザ名が3文字未満のとき
    """
    value: Final[str]

    def __post_init__(self):
        if len(self.value) < 3: raise ArgumentException("ユーザ名は3文字以上です", str(self.value))

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