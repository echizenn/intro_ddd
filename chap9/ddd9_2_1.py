"""
9.2.1節のコードの説明
"""
from typing import Final
import dataclasses

from chap4.ddd4_4_1 import UserName

# リスト9.9
@dataclasses.dataclass
class User:
    """
    オブジェクトにセッターを用意する
    setterを利用できるように、Finalという型アノテーションをなくした
    """
    name: UserName