"""
5.8.2節のコードの説明
"""
from abc import ABCMeta, abstractmethod
from typing import List

from chap4.ddd4_4_1 import User, UserId, UserName


class IUserRepository(metaclass=ABCMeta):
    """
    Userクラスのリポジトリインターフェース
    """

    # リスト5.26
    @abstractmethod
    def find(self, id: UserId) -> User:
        """
        ユーザidによるインスタンスの復元
        識別子によって検索されるメソッド

        Args:
            id (UserId): 復元したいユーザid
        
        Returns:
            User: 復元されたUserインスタンス
        """
        pass

    # リスト5.27
    @abstractmethod
    def find_all(self) -> List[User]:
        """
        すべてのオブジェクトを再構築するメソッド

        Args: None
        
        Returns:
            List[User]: すべてのUserインスタンス
        """
        pass

    # リスト5.28
    @abstractmethod
    def find_by_user_name(self, name: UserName) -> User:
        """
        探索に適したメソッド
        Pythonではオーバーロードがサポートされていないので、命名によりバリエーションを増やす
        """
        pass
