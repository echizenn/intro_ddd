"""
6.2.1節のコードの説明
この節はこれまでの振り返りなのであまり説明はないです
"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import uuid
from typing import Final

# リスト6.1
@dataclass
class User:
    """
    ユーザを表すエンティティ

    Attributes:
        name (UserName): ユーザ名
        id (UserId): ユーザid

    Note:
        初めての生成はidの指定なし
        再構築の時はidとname両方指定する
    """
    name: UserName
    id: UserId = uuid.uuid1()

    def change_name(self, name: UserName):
        """
        ユーザ名を変えるメソッド

        Args:
            name (UserName): ユーザ名
        """
        self.name = name

# リスト6.2
class UserId:
    """
    Userクラスが利用している値オブジェクトの定義

    Attributes:
        _value (str): id文字列

    Raises:
        ValueError: valueが空文字の時
    """
    def __init__(self, value: str):
        if not value: raise ValueError("valueが空文字です")
        self._value = value

    @property
    def value(self):
        return self._value

class UserName:
    """
    Userクラスが利用している値オブジェクトの定義

    Attributes:
        _value (str): 名前

    Raises:
        ValueError: valueが3文字以上20文字以下でないとき
    """
    def __init__(self, value: str):
        if not 3 <= len(value) <= 20:
            raise ValueError("ユーザ名は3文字以上20文字以下です。")
        self._value = value

    @property
    def value(self):
        return self._value

# リスト6.3
@dataclass
class UserService:
    """
    ユーザのドメインサービス

    Attributes:
        user_repository (Final[IUserRepository]): レポジトリ
    """
    user_repository: Final[IUserRepository]

    def exists(self, user: User) -> bool:
        """
        ユーザがレポジトリに存在しているか

        Args:
            user (User): 重複確認したいユーザ

        Returns:
            bool: 重複しているか否か
        """
        duplicated_user: bool = self.user_repository.find(user.name)

        return duplicated_user is not None

# リスト6.4
class IUserRepository(metaclass=ABCMeta):
    """
    ユーザのリポジトリ
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
    def find_by_name(self, name: UserName) -> User:
        """
        ユーザ名によるインスタンスの復元

        Args:
            name (UserName): 探したいユーザ名
        
        Returns:
            User: 見つかったUserインスタンス(ない場合はNone)
        """
        pass

    @abstractmethod
    def find_by_id(self, id: UserName) -> User:
        """
        ユーザ名によるインスタンスの復元

        Args:
            id (UserId): 探したいユーザid
        
        Returns:
            User: 見つかったUserインスタンス(ない場合はNone)
        """
        pass

    @abstractmethod
    def delete(self, user: User):
        """
        Userインスタンスを削除

        Args:
            user (User): 削除したいUserインスタンス

        Returns: None
        """
        pass