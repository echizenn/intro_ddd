"""
5.2節のコードの説明
"""
import dataclasses
from typing import Optional

from chap4.ddd4_4_1 import User, UserName

# リスト5.3
@dataclasses.dataclass
class Program:
    """
    レポジトリを利用したユーザ作成処理

    Attributes:
        _user_repository (IUserRepository): ユーザレポジトリ

    Note:
        コードの意図がわかりやすくなっている
    """
    _user_repository: IUserRepository

    def create_user(self, user_name: str):
        """
        ユーザ作成処理

        Args:
            user_name (str): ユーザ名

        Returns: None

        Raises:
            Exception: ユーザ名が重複しているとき
        """
        user: User = User(UserName(user_name))

        user_service: UserService = UserService(self._user_repository)
        if user_service.exists(user):
            raise Exception(f"{user_name}はすでに存在しています")

        self._user_repository.save(user)

# リスト5.4
@dataclasses.dataclass
class UserService:
    """
    レポジトリを利用したドメインサービス

    Attributes:
        _user_repository (IUserRepository): ユーザレポジトリ

    Note:
        コードの意図がわかりやすくなっている
    """
    _user_repository: IUserRepository

    def exists(self, user: User) -> bool:
        """
        userが存在しているか確認

        Args:
            user (User): 重複を確認したいユーザ
        
        Returns:
            bool: 重複しているか否か
        """
        # findは存在する場合、Userインスタンスを返す
        found: Optional[User] = self._user_repository.find(user.name)

        return found != None
