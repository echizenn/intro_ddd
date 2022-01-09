"""
9.3節のコードの説明
"""
import dataclasses
from typing import Final

from chap4.ddd4_4_1 import UserId, UserName

# リスト9.13
# サークルを生成する
circle = Circle(
    user.Id, # ゲッターによりユーザのIDを取得
    CircleName("my circle")
)

# リスト9.14
@dataclasses.dataclass
class User:
    _id: Final[UserId]

    # ファクトリとして機能するメソッド
    def create_circle(self, circle_name: CircleName) -> Circle:
        return Circle(
            id,
            circle_name
        )