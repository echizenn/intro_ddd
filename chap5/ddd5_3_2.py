"""
5.3節のコードの説明
"""
from abc import ABCMeta, abstractmethod

from chap4.ddd4_4_1 import User, UserName

# リスト5.6
class IUserRepository(metaclass=ABCMeta):
    """
    リポジトリに重複確認メソッドを追加した場合

    Attributes: None
    """
    @abstractmethod
    def save(self, user: User):
        """
        Userインスタンスを保存

        Args:
            user (User): 保存したいUserインスタンス

        Returns: None
        """
        pass

    @abstractmethod
    def find(self, name: UserName) -> User:
        """
        ユーザ名によるインスタンスの復元

        Args:
            name (UserName): 復元したいユーザ名
        
        Returns:
            User: 復元されたUserインスタンス
        """
        pass

    @abstractmethod
    def exists(self, user: User) -> bool:
        """
        重複チェック

        Args:
            user (User): 重複チェックしたいユーザ
        
        Returns:
            bool: 重複しているか否か

        Note:
            オブジェクトの永続化というリポジトリの責務を超えている
        """
        pass

# リスト5.7
class UserService:
    """
    レポジトリを利用したドメインサービス

    Attributes:
        _user_repository (IUserRepository): ユーザレポジトリ

    Note:
        リスト5.6を利用するとドメインサービスが主体にならない
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
        # ユーザ名により重複確認を行うという知識は失われている
        return self._user_repository.exists(user)