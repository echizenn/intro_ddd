"""
5.3節のコードの説明
"""
from abc import ABCMeta, abstractmethod

from chap4.ddd4_4_1 import User, UserName

# リスト5.8
class IUserRepository(metaclass=ABCMeta):
    """
    Userクラスのリポジトリインターフェース

    Note:
        リポジトリに重複確認を定義する場合
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
    def exists(self, name: UserName) -> bool:
        """
        重複チェック

        Args:
            name (UserName): 重複チェックしたいユーザ名
        
        Returns:
            bool: 重複しているか否か

        Note:
            オブジェクトの永続化というリポジトリの責務を超えている
        """
        pass