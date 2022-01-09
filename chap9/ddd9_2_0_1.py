"""
9.2節のコードの説明
"""
import dataclasses
import uuid
from typing import Final, Optional

from chap4.ddd4_4_1 import UserId, UserName

# リスト9.1
class User():
    """
    ユーザの識別子はコンストラクタで生成される

    Attributes:
        id (UserId): ユーザid
        name (UserName): ユーザ名
    """
    # 本のGuid.NewGuid().ToString()でユニークなIDを取得している
    # pythonならuuidモジュールを使えばよい
    def __init__(self, name: UserName, id: Optional[int]=None):
        self.id: Final[UserId] = dataclasses.field(default=uuid.uuid1(), init=False) if id is None else id
        self.name: Final[UserName] = name