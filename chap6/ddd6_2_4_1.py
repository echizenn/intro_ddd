"""
6.2.4節のコードの説明
"""
from dataclasses import dataclass
from typing import Final, Optional

from ddd6_2_1 import IUserRepository, UserService, User, UserName, UserId

# リスト6.15
@dataclass
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
            ValueError: 同一ユーザが存在している場合
        """
        user : User = User(UserName(name))

        if self._user_service.exists(user):
            raise ValueError("ユーザはすでに存在しています")

        self._user_repository.save(user)

    def get(self, user_id: str) -> Optional[UserData]:
        """
        戻り値としてドメインオブジェクトを公開したユーザ情報取得メソッド

        Args:
            user_id (str): ユーザid
        
        Returns:
            Optional[UserData]: ユーザのデータ転送用オブジェクト

        Note:
            ドメインで変更があっても影響を受けなくなった
        """
        target_id: UserId = UserId(user_id)
        user: User = self._user_repository.find(target_id)

        if user is None: return None
        
        return UserData(user)

    def update(self, user_id: str, name: str):
        """
        ユーザ名の変更を行う更新処理

        Args:
            user_id (str): 変更したいユーザのid
            name (str): 変更後のユーザ名

        Returns: None

        Raises:
            ValueError: 存在しないユーザのidを指定した場合
            ValueError: 同一ユーザが存在している場合
        """
        target_id: UserId = UserId(user_id)
        user: Optional[User] = self._user_repository.find(target_id)

        if user is None: raise ValueError("user_idの値が不適切です")

        new_user_name: UserName = UserName(name)
        user.change_name(new_user_name)
        if self._user_service.exists(user):
            raise ValueError("そのユーザはすでに存在しています")

        self._user_repository.save(user)
        