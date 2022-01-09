"""
10.2節のコードの説明
"""
import dataclasses
from typing import Final

from chap4.ddd4_4_1 import UserName
from chap5.ddd5_3_1 import IUserRepository
from chap9.ddd9_2_0_3 import IUserFactory

# リスト10.1
@dataclasses.dataclass
class UserApplicationService():
    """
    ユーザ登録処理のコード
    """
    _user_factory: Final[IUserFactory]
    _user_repository: Final[IUserRepository]
    _user_service: Final[UserService]

    def register(self, command: UserRegisterCommand):
        user_name = UserName(command.name)
        # ファクトリによってインスタンスを生成する
        user = self._user_factory.create(user_name)

        if self._user_service.exists(user):
            raise ValueError("そのユーザはすでに存在しています")
        self._user_repository.save(user)