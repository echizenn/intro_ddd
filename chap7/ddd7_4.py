"""
7.4節のコードの説明
"""
from dataclasses import dataclass

from ddd7_2_1 import IUserRepository


# リスト7.5
@dataclass
class UserApplicationService:
    _user_repository: IUserRepository = InMemoryUserRepository()


# リスト7.6
@dataclass
class UserApplicationService:
    _user_repository: IUserRepository = UserRepository()
