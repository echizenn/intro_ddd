"""
6.2.1節のコードの説明
この節はこれまでの振り返りなのであまり説明はないです
"""
from abc import ABCMeta, abstractmethod
import dataclasses
import uuid
from typing import Final, Optional

# リスト6.2
@dataclasses.dataclass(frozen=True)
class UserId:
    """
    Userクラスが利用している値オブジェクトの定義

    Attributes:
        value (str): id文字列

    Raises:
        ArgumentException: valueが空文字の時
    """
    value: Final[str]

    def __post_init__(self):
        if not self.value: raise ArgumentException("valueが空文字です")


@dataclasses.dataclass(frozen=True)
class UserName:
    """
    Userクラスが利用している値オブジェクトの定義

    Attributes:
        value (str): 名前

    Raises:
        ArgumentException: valueが3文字以上20文字以下でないとき
    """
    value: Final[str]

    def __post_init__(self):
        if not 3 <= len(self.value) <= 20:
            raise ArgumentException("ユーザ名は3文字以上20文字以下です。", str(self.value))

# リスト6.1
@dataclasses.dataclass
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
    _name: UserName
    _id: Final[UserId] = dataclasses.field(default_factory=lambda: UserId(uuid.uuid4()), init=False)

    @property
    def name(self) -> UserName:
        return self._name

    @property
    def id(self) -> UserId:
        return self._id

    def change_name(self, name: UserName):
        """
        ユーザ名を変えるメソッド

        Args:
            name (UserName): ユーザ名
        """
        self.name = name

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
    def find_by_name(self, name: UserName) -> Optional[User]:
        """
        ユーザ名によるインスタンスの復元

        Args:
            name (UserName): 探したいユーザ名
        
        Returns:
            Optional[User]: 見つかったUserインスタンス(ない場合はNone)
        """
        pass

    @abstractmethod
    def find_by_id(self, id: UserName) -> Optional[User]:
        """
        ユーザ名によるインスタンスの復元

        Args:
            id (UserId): 探したいユーザid
        
        Returns:
            Optional[User]: 見つかったUserインスタンス(ない場合はNone)
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

# リスト6.3
@dataclasses.dataclass(frozen=True)
class UserService:
    """
    ユーザのドメインサービス

    Attributes:
        user_repository (Final[IUserRepository]): レポジトリ
    """
    _user_repository: Final[IUserRepository]

    def exists(self, user: User) -> bool:
        """
        ユーザがレポジトリに存在しているか

        Args:
            user (User): 重複確認したいユーザ

        Returns:
            bool: 重複しているか否か
        """
        duplicated_user: bool = self._user_repository.find(user.name)

        return duplicated_user is not None