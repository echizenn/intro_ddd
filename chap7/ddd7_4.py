"""
7.4節のコードの説明
"""
import dataclasses

from ddd7_2_1 import IUserRepository, UserRepository


# リスト7.5
@dataclasses.dataclass
class UserApplicationService:
    _user_repository: IUserRepository = InMemoryUserRepository()


# リスト7.6
@dataclasses.dataclass
class UserApplicationService:
    _user_repository: IUserRepository = UserRepository()
