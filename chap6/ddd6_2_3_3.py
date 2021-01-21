"""
6.2.3節のコードの説明
"""
from dataclasses import dataclass
from typing import Final

from ddd6_2_1 import IUserRepository, UserService, User, UserName, UserId
from ddd6_2_3_2 import UserData

# リスト6.10
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

    def get(self, user_id: str) -> UserData:
        """
        戻り値としてドメインオブジェクトを公開したユーザ情報取得メソッド

        Args:
            user_id (str): ユーザid
        
        Returns:
            UserData: ユーザのデータ転送用オブジェクト

        Note:
            外部公開するパラメータは追加されたときの変化
            UserDataインスタンスを使う全ての箇所で変更が必要になる
        """
        target_id: UserId = UserId(user_id)
        user: User = self._user_repository.find(target_id)

        # user_data: UserData = UserData(user.id.value, user.name.value)
        # コンストラクタの引数が増える
        user_data: UserData = UserData(user.id.value, user.name.value,
                                                    user.mail_address.value)
        return user_data