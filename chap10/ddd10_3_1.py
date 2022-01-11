"""
10.3.1節のコードの説明
"""
import dataclasses
from typing import Final

from chap4.ddd4_4_1 import UserName
from chap5.ddd5_3_1 import IUserRepository
from chap9.ddd9_2_0_3 import IUserFactory

# リスト10.2
@dataclasses.dataclass
class UserApplicationService():
    """
    ユニークキー制約で重複しないことが担保され重複確認が不要になる
    """
    _user_factory: Final[IUserFactory]
    _user_repository: Final[IUserRepository]

    def register(self, command: UserRegisterCommand):
        user_name = UserName(command.name)
        user = self._user_factory.create(user_name)

        self._user_repository.save(user)