"""
9.2節のコードの説明
"""
import dataclasses
from typing import Final
import uuid

from chap4.ddd4_4_1 import UserId, UserName

# リスト9.1
@dataclasses.dataclass
class User():
    """
    ユーザの識別子はコンストラクタで生成される

    Attributes:
        name (UserName): ユーザ名
        id (UserId): ユーザid
    """
    # 本のGuid.NewGuid().ToString()でユニークなIDを取得している
    # pythonならuuidモジュールを使えばよい
    # dataclasses活用するなら必ず必要な属性の方を先に定義しなければならない
    name: Final[UserName]
    id: Final[UserId] = dataclasses.field(default_factory=lambda: UserId(uuid.uuid4())) # idをインスタンスを作る際に指定することも可能