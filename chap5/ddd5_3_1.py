"""
5.3節のコードの説明
"""
from abc import ABCMeta, abstractmethod

# リスト5.5
class IUserRepository(metaclass=ABCMeta):
    """
    Userクラスのリポジトリインターフェース
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