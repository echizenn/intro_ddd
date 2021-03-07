"""
6.2.3節のコードの説明
"""
from dataclasses import dataclass
from typing import Final, Optional

from ddd6_2_1 import IUserRepository, UserService, User, UserName, UserId


# リスト6.11, 13
class UserData:
    """
    Userクラスのデータを公開するために定義されたDTO

    Attributes:
        source (User): ドメインオブジェクト

    Note:
        変更箇所がUserDataオブジェクトにまとめられることを確認
    """
    def __init__(self, source: User):
        self._id: str = source.id.value
        self._name: str = source.name.value
        self._mail_address: str = source.mail_address.value # 属性への代入処理

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    # 追加された属性
    @property
    def mail_address(self) -> str:
        return self._mail_address

# リスト6.12
def list6_12(user: User):
    """
    専用のコンストラクタを利用したときのデータ移し替えを行うコード

    Args:
        user (User): ユーザオブジェクト

    Returns: None
    """
    user_data: UserData = UserData(user)

# リスト6.14
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
        user: User = self._user_repository.(target_id)

        if user is None: return None
        
        return UserData(user)