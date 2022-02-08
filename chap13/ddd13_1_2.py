"""
13.1.2節のコードの説明
"""
import dataclasses
import datetime
from typing import Final

from chap13.ddd13_1_1_2 import Circle

# リスト13.4
@dataclasses.dataclass(frozen=True)
class CircleFullException:
    """
    サークルが満員かどうかを評価する仕様

    Attributes:
        _user_repository(IUserRepository): ユーザレポジトリ

    Note:
        複雑な評価手順をカプセル化することができる
    """
    _user_repository: Final[IUserRepository]

    def is_satisfied_by(self, circle: Circle) -> bool:
        users = self._user_repository.find(circle.members())
        premium_user_number = len([user for user in users if user.is_premium])
        circle_upper_limit = 30 if premium_user_number < 10 else 50
        return self.count_members() >= circle_upper_limit

# リスト13.5
@dataclasses.dataclass(frozen=True)
class CircleApplicationService:
    """
    仕様を利用する

    Note:
        ドメインについて直接のコードの記述がなくなる
    """
    _circle_repository: Final[ICircleRepository]
    _user_repository: Final[IUserRepository]

    def join(self, command: CircleJoinCommand):
        circle_id = CircleId(command.circle_id)
        circle = self._circle_repository.find(circle_id)

        circle_full_specification = CircleFullSpecification(self._user_repository)
        if circle_full_specification.is_satisfied_by(circle):
            raise CircleFullException(circle_id)

        pass

# リスト13.6
class Circle:
    """
    メソッドにまみれた定義
    """
    def is_full(self) -> bool:
        pass

    def is_popular(self) -> bool:
        pass

    def is_anniversary(self, date: datetime.date) -> bool:
        pass

    def is_recruiting(self) -> bool:
        pass

    def is_locked(self) -> bool:
        pass

    def is_private(self) -> bool:
        pass

    def join(self, user: User):
        pass