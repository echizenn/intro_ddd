"""
6.3節のコードの解説
"""
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Optional

from ddd6_2_1 import UserService, User, UserName, UserId

# リスト6.24
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
    def find_by_mail_address(self, mail_address: MailAddress) -> Optional[User]:
        """
        メールアドレスによるインスタンスの復元

        Args:
            mail_address (MailAddress): 探したいユーザのメールアドレス
        
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


@dataclasses.dataclass
class UserApplicationService:
    """
    ユーザのアプリケーションサービス

    Attributes:
        _user_repository (IUserRepository): ユーザのレポジトリ
        _user_service (UserService): ユーザのドメインサービス
    """
    _user_repository: Final[IUserRepository]
    _user_service: Final[UserService]

    # リスト6.25
    def register(self, name: str, raw_mail_address: str):
        """
        ユーザ登録

        Args:
            name (str): ユーザ名
            raw_mail_address (str): メールアドレス
        
        Returns: None

        Raises:
            ValueError: 同一ユーザが存在している場合
        """
        # メールアドレスに夜重複確認を行うように変更された
        mail_address: MailAddress = MailAddress(raw_mail_address)
        duplicated_user: Optional[User] = self._user_repository.find_by_mail_address(
            mail_address
        )
        if duplicated_user is not None:
            raise ValueError("ユーザはすでに存在しています")

        user_name: UserName = UserName(name)
        user: User = User(user_name, mail_address)

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
        user: User = self._user_repository.find_by_id(target_id)

        if user is None: return None
        
        return UserData(user)

    # リスト6.26
    def update(self, command: UserUpdateCommand):
        """
        ユーザ名の変更を行う更新処理

        Args:
            command (UserUpdateCommand): コマンドオブジェクト

        Returns: None

        Raises:
            ValueError: 存在しないユーザのidを指定した場合
            ValueError: 同一ユーザが存在している場合

        Note:
            ユーザ情報更新処理も同様に重複確認のロジックを修正する必要がある
            重複確認をする箇所が点在していて修正箇所の見落としが起こる可能性が高まる
        """
        target_id: UserId = UserId(command.id)
        user: Optional[User] = self._user_repository.find_by_id(target_id)

        if user is None: raise ValueError("user_idの値が不適切です")

        name: Optional[str] = command.name
        if name is not None:
            # ユーザ名での重複確認はなくなる
            new_user_name: UserName = UserName(name)
            user.change_name(new_user_name)

        mail_address: Optional[str] = command.mail_address
        if mail_address is not None:
            # メールアドレスで重複確認を行うようになる
            new_mail_address: MailAddress = MailAddress(mail_address)
            duplicated_user: Optional[User] = self._user_repository.find_by_mail_address(
                new_mail_address
            )
            if duplicated_user is not None:
                raise ValueError("同じメールアドレスのユーザが存在しています")
            user.change_mail_address(new_mail_address)
        
        self._user_repository.save(user)

    def delete(command: UserUpdateCommand):
        """
        退会処理

        Args:
            command (UserUpdateCommand): 退会したいユーザのコマンドオブジェクト

        Returns: None

        Raises:
            ValueError: 存在しないユーザのuser_idの場合
        """
        target_id: UserId = UserId(command.id)
        user: User = self._user_repository.find_by_id(target_id)

        if user is None: raise ValueError("user_idの値が不適切です")

        self._user_repository.delete(user)