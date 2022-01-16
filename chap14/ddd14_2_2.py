"""
14.2.2節のコードの説明
"""
import dataclasses
from typing import Final

# リスト14.5
@dataclasses.dataclass
class UserApplicationService:
    """
    ユーザアプリケーションサービスのコード
    """
    _user_repository: Final[IUserRepository]
    _user_service: Final[UserService]

    def update(self, command: UserUpdateCommand):
        with TransactionScope() as transaction:
            id = UserId(command.id)
            user = self._user_repository.find(id)
            if user is None: raise UserNotFoundException(id)

            if command.name is not None:
                name = UserName(command.name)
                user.change_name(name)

                if self._user_service.exists(user): raise CanNotRegisterUserException(user, "ユーザは既に存在しています。")

            # セカンダリリポートであるIUserRepositoryの処理を呼び出す
            # 処理は実体であるセカンドリアダプタに移る
            self._user_repository.save(user)

            transaction.complete()