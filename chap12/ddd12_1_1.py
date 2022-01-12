"""
12.1.1節のコードの説明
"""
import dataclasses
from typing import List

from chap2.ddd2_5_3 import User, UserName


# リスト12.1
# ユーザ名の変更はUserオブジェクトに依頼する
user_name = UserName("NewName")

# NG
user.name = user_name

# OK
user.change_name(user_name)

# リスト12.2
# 第１１章で登場したサークルにメンバーを追加するコード
circle.members.append(member)

# リスト12.3
@dataclasses.dataclass
class Circle:
    """
    メンバーを追加するコードをエンティティに追加
    """
    ＿id: Final[CircleId]
    _owner: User
    # メンバーは非公開にできる
    _members: List[User]

    def join(self, member: User):
        if member is None: raise ArgumentNullException(member)

        if len(self._members) >= 29: raise CircleFullException(id)

        self._members.append(member)

# リスト12.4
# メンバー追加のためにCircleのメソッドを呼び出す
circle.join(user)

# リスト12.5
pass