"""
13.1.1節のコードの説明
"""
import dataclasses
from typing import Final, List

# リスト13.2
@dataclasses.dataclass(frozen=True)
class CircleApplicationService:
    """
    サークルのメンバー上限数は条件によって変更される
    """
    _circle_repository: Final[ICircleRepository]
    _user_repository: Final[IUserRepository]

    def join(self, command: CircleJoinCommand):
        circle_id = CircleId(command.circle_id)
        circle = self._circle_repository.find(circle_id)

        users = self._user_repository.find(circle.members)
        # サークルに所属しているプレミアムユーザの人数により上限が変わる
        premium_user_number = len([user for user in users if user.is_premium])
        circle_upper_limit = 30 if premium_user_number < 10 else 50
        if circle.count_members() >= circle_upper_limit:
            raise CircleFullException(circle_id)

        pass

# リスト13.3
@dataclasses.dataclass
class Circle:
    # プレミアムユーザの人数を探したいが保持しているのはUserIdのコレクションだけ
    _members: List[UserId]

    def members(self) -> List[UserId]:
        return self._members

    # ユーザのレポジトリを受け取る？
    def is_full(self, user_repository: IUserRepository) -> bool:
        users = user_repository.find(self._members)
        premium_user_number = len([user for user in users if user.is_premium])
        circle_upper_limit = 30 if premium_user_number < 10 else 50
        return self.count_members() >= circle_upper_limit