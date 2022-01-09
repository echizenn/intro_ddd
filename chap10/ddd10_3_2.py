"""
10.3.2節のコードの説明
"""
import dataclasses
from typing import Final

from chap4.ddd4_4_1 import User
from chap9.ddd9_2_2 import IUserRepository

# リスト10.3
@dataclasses.dataclass
class UserService:
    """
    重複チェックの対象をメールアドレスにしてしまった
    """
    _user_repository: Final[IUserRepository]

    def exists(self, user: User):
        duplicated_user = self._user_repository.find(user.mail)
        return duplicated_user is not None