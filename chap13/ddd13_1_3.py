"""
13.1.3節のコードの説明
"""
import dataclasses
from typing import Final, List

# リスト13.7
@dataclasses.dataclass(frozen=True)
class CircleMembers:
    """
    サークルに所属するメンバーを表すファーストクラスコレクション
    """
    _id: Final[CircleId]
    _owner: Final[User]
    _members: Final[List[User]]

    @property
    def id(self) -> CircleId:
        return self._id

    def count_members(self) -> int:
        return len(self._members) + 1

    def count_premium_members(self, contains_owner: bool=True):
        premium_user_number = len([member for member in self._members if member.is_premium])
        if contains_owner:
            return premium_user_number + int(self._owner.is_premium)
        else:
            return premium_user_number

# リスト13.8
class CircleMembersFullSpecification:
    """
    CircleMembersを利用した仕様
    """
    def is_satisfied_by(self, members: CircleMembers) -> bool:
        premium_user_number = members.count_premium_members(False)
        circle_upper_limit = 30 if premium_user_number < 10 else 50
        return members.count_members() >= circle_upper_limit

# リスト13.9
def list13_9(user_repository: IUserRepository, circle: Circle):
    """
    ファーストクラスコレクションに詰め替える

    Note:
        ドメインオブジェクトを入出力で使わないようになった
    """
    owner = user_repository.find(circle.owner)
    members = user_repository.find(circle.members)
    circle_members = CircleMembers(circle.id, owner, members)
    circle_full_spec = CircleMembersFullSpecification()
    if circle_full_spec.is_satisfied_by(circle_members):
        pass