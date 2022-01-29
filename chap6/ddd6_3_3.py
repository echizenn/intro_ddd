"""
6.3節のコードの解説
"""
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Optional

from ddd6_2_1 import IUserRepository, User, UserName, UserId


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

    # リスト6.27
    def register(self, name: str, mail_address: str):
        """
        ユーザ登録

        Args:
            name (str): ユーザ名
            raw_mail_address (str): メールアドレス
        
        Returns: None

        Raises:
            CanNotRegisterUserException: 同一ユーザが存在している場合

        Note:
            ドメインサービスを利用するように変更
        """
        user: User = User(UserName(name), MailAddress(mail_address))

        if self._user_service.exists(user):
            raise CanNotRegisterUserException(user, "ユーザは既に存在しています")

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

    # リスト6.28
    def update(self, command: UserUpdateCommand):
        """
        ユーザ名の変更を行う更新処理

        Args:
            command (UserUpdateCommand): コマンドオブジェクト

        Returns: None

        Raises:
            UserNotFoundException: 存在しないユーザのidを指定した場合
            CanNotRegisterUserException: 同一ユーザが存在している場合

        Note:
            ドメインサービスを利用するようにした
            個人的には90行目のif文の中でexistsを確認する意味がわからない
        """
        target_id: UserId = UserId(command.id)
        user: Optional[User] = self._user_repository.find_by_id(target_id)

        if user is None: raise UserNotFoundException(target_id)

        name: Optional[str] = command.name
        if name is not None:
            new_user_name: UserName = UserName(name)
            user.change_name(new_user_name)
            if self._user_service.exists(user):
                raise CanNotRegisterUserException(user, "ユーザは既に存在しています")

        mail_address: Optional[str] = command.mail_address
        if mail_address is not None:
            new_mail_address: MailAddress = MailAddress(mail_address)
            user.change_mail_address(new_mail_address)
        
        self._user_repository.save(user)

    def delete(self, command: UserUpdateCommand):
        """
        退会処理

        Args:
            command (UserUpdateCommand): 退会したいユーザのコマンドオブジェクト

        Returns: None

        Raises:
            UserNotFoundException: 存在しないユーザのuser_idの場合
        """
        target_id: UserId = UserId(command.id)
        user: User = self._user_repository.find_by_id(target_id)

        if user is None: raise UserNotFoundException(target_id)

        self._user_repository.delete(user)


# リスト6.29
@dataclasses.dataclass
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
        
        Note:
            ドメインサービス上でユーザの重複に関するルールを変更する
        """
        # 重複のルールをユーザ名からメールアドレスに変更
        # duplicated_user: bool = self.user_repository.find(user.name)
        duplicated_user: bool = self.user_repository.find(user.mail_address)

        return duplicated_user is not None
