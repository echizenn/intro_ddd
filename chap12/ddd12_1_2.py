"""
12.1.2節のコードの説明
"""
import dataclasses

from chap2.ddd2_5_3 import User


# リスト12.6
# メンバーを追加する際の上限チェックを行うコード
if len(circle.members()) >= 29:
    raise CircleFullException(id)

# リスト12.7
@dataclasses.dataclass
class Circle:
    """
    デメテルの法則にしたがいオブジェクトにふるまいを追加する
    """
    ＿id: Final[CircleId]
    # メンバー一覧は非公開にできる
    _members: List[User]

    def is_full(self) -> bool:
        return len(self._members) >= 29

    def join(self, member: User):
        if member is None: raise ArgumentNullException(member)

        if self.is_full(): raise CircleFullException(id)

        self._members.append(member)

# リスト12.8
# リスト12.7のIsFullメソッドを利用して上限チェックを行う
if circle.is_full(): raise CircleFullException(circle_id)

# リスト12.9
@dataclasses.dataclass
class Circle:
    """
    上限数の変更
    """
    ＿id: Final[CircleId]
    _members: List[User]

    def is_full(self) -> bool:
        # return len(self._members) >= 29
        return len(self._members) >= 49