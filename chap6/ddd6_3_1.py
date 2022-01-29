"""
6.3節のコードの解説
"""
import dataclasses
from typing import Optional

from ddd6_2_1 import IUserRepository, UserService, User, UserName, UserId

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

    # リスト6.22
    def register(self, name: str):
        """
        ユーザ登録

        Args:
            name (str): ユーザ名
        
        Returns: None

        Raises:
            CanNotRegisterUserException: 同一ユーザが存在している場合

        Note:
            アプリケーションサービスに重複に関するルールが記述されているユーザ登録処理
        """
        # 重複確認を行うコード
        user_name: UserName = UserName(name)
        duplicated_user: Optional[User] = self._user_repository.find_by_name(
            user_name
        )
        if duplicated_user is not None:
            raise CanNotRegisterUserException(user, "ユーザはすでに存在しています")

        user: User = User(user_name)
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

    # リスト6.23
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
            ユーザ情報更新処理に置いても重複確認を行う必要がある
        """
        target_id: UserId = UserId(command.id)
        user: Optional[User] = self._user_repository.find_by_id(target_id)

        if user is None: raise UserNotFoundException(target_id)

        name: Optional[str] = command.name
        if name is not None:
            # 重複確認を行うコード
            new_user_name: UserName = UserName(name)
            duplicated_user: User = self._user_repository.find_by_name(
                new_user_name
            )
            if duplicated_user is not None:
                raise CanNotRegisterUserException(user, "ユーザはすでに存在しています")
            user.change_name(new_user_name)

        mail_address: Optional[str] = command.mail_address
        if mail_address is not None:
            new_mail_address: MailAddress = MailAddress(mail_address)
            user.change_mail_address(new_mail_address)
        
        self._user_repository.save(user)

    def delete(command: UserUpdateCommand):
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