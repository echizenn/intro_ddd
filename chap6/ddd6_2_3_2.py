"""
6.2.3節のコードの説明
"""
import dataclasses
from typing import Final

from ddd6_2_1 import IUserRepository, UserService, User, UserName, UserId

# リスト6.8
@dataclasses.dataclass
class UserData:
    """
    Userクラスのデータを公開するために定義されたDTO

    Attributes:

    """
    _id: str
    _name: str

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

# リスト6.9
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

    def get(self, user_id: str) -> UserData:
        """
        戻り値としてドメインオブジェクトを公開したユーザ情報取得メソッド

        Args:
            user_id (str): ユーザid
        
        Returns:
            UserData: ユーザのデータ転送用オブジェクト
        """
        target_id: UserId = UserId(user_id)
        user: User = self._user_repository.find_by_id(target_id)

        user_data: UserData = UserData(user.id.value, user.name.value)
        return user_data