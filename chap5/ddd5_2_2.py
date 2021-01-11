"""
5.2節のコードの説明
"""
from typing import Optional

# リスト5.3
class Program:
    """
    レポジトリを利用したユーザ作成処理

    Attributes:
        _user_repository (IUserRepository): ユーザレポジトリ

    Note:
        コードの意図がわかりやすくなっている
    """
    def __init__(self, user_repository: IUserRepository):
        self._user_repository: IUserRepository = user_repository

    def create_user(self, user_name: str):
        """
        ユーザ作成処理

        Args:
            user_name (str): ユーザ名

        Returns: None

        Raises:
            ValueError: ユーザ名が重複しているとき
        """
        user: User = User(UserName(user_name))

        user_service: UserService = UserService(self._user_repository)
        if user_service.exists(user):
            raise ValueError("{}はすでに存在しています".format(user_name))

        _user_repository.save(user)

# リスト5.4
class UserService:
    """
    レポジトリを利用したドメインサービス

    Attributes:
        _user_repository (IUserRepository): ユーザレポジトリ

    Note:
        コードの意図がわかりやすくなっている
    """
    def __init__(self, user_repository: IUserRepository):
        self._user_repository: IUserRepository = user_repository

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
