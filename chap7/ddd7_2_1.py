"""
7.2節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses

from chap6.ddd6_2_1 import UserId

# リスト7.1
class ObjectA:
    """
    ObjectAはObjectBに依存する
    """
    _object_b: ObjectB


# リスト7.2
class IUserRepository(metaclass=ABCMeta):
    """
    ユーザーレポジトリのインターフェース
    """

    @abstractmethod
    def find(id: UserId):
        """
        ユーザーを探す

        Args:
            id(UserId): ユーザーid
        """
        pass


class UserRepository(IUserRepository):
    """
    ユーザーレポジトリ
    IUserRepositoryに依存している
    """
    def find(id: UserId):
        """
        ユーザーを探す

        Args:
            id(UserId): ユーザーid
        """
        # 省略
        pass


# リスト7.3
@dataclasses.dataclass
class UserApplicationService:
    """
    ユーザーのアプリケーションサービス
    """
    _user_repository: UserRepository
