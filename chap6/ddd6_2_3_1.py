"""
6.2.3節のコードの説明
"""
import dataclasses
from typing import Final

from ddd6_2_1 import IUserRepository, UserService, User, UserName, UserId

# リスト6.6
@dataclasses.dataclass(frozen=True)
class UserApplicationService:
    """
    ユーザのアプリケーションサービス

    Attributes:
        _user_repository (IUserRepository): ユーザのレポジトリ
        _user_service (UserService): ユーザのドメインサービス
    """
    _user_repository: Final[IUserRepository]
    _user_service: Final[UserService]

    def register(self, name: str):
        """
        ユーザ登録

        Args:
            name (str): ユーザ名
        
        Returns: None

        Raises:
            CanNotRegisterUserException: 同一ユーザが存在している場合
        """
        user : User = User(UserName(name))

        if self._user_service.exists(user):
            raise CanNotRegisterUserException(user, "ユーザはすでに存在しています")

        self._user_repository.save(user)

    def get(self, user_id: str) -> User:
        """
        戻り値としてドメインオブジェクトを公開したユーザ情報取得メソッド

        Args:
            user_id (str): ユーザid
        
        Returns:
            User: ユーザオブジェクト

        Note:
            とてもシンプルなコードにはなる
        """
        target_id: UserId = UserId(user_id)
        user: User = self._user_repository.find_by_id(target_id)

        return user

# リスト6.7
@dataclasses.dataclass(frozen=True)
class Client:
    """
    ドメインオブジェクトのメソッドの意図せぬ呼び出し

    Attributes:
        _user_application_service (UserApplicationService):
                                                    ユーザアプリケーションサービス
    """
    _user_application_service: UserApplicationService

    def change_name(self, id: str, name: str):
        """
        ユーザ名の変更

        Args:
            id (str): 変更したいユーザのユーザid
            name (str): 変更後のユーザ名
        
        Returns: None

        Note:
            ドメインオブジェクトの振る舞いを呼び出すのはアプリケーションサービスの役目なのに
            それ以外のオブジェクトでもドメインオブジェクトの振る舞いを呼び出せてしまう
        """
        target: User = self._user_application_service.get(id)
        new_name: UserName = UserName(name)
        target.change_name(new_name)