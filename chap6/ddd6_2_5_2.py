"""
6.2.5節のコードの説明
"""
from dataclasses import dataclass
from typing import Final, Optional

from ddd6_2_1 import IUserRepository, UserService, User, UserName, UserId
from ddd6_2_4_3  import UserUpdateCommand

# リスト6.21
@dataclass
class UserApplicationService:
    """
    ユーザのアプリケーションサービス

    Attributes:
        _user_repository (IUserRepository): ユーザのレポジトリ
        _user_service (UserService): ユーザのドメインサービス
    """
    _user_repository: Final[IUserRepository]
    _user_service: Final[UserService]

    def register(self, name: str):
        """
        ユーザ登録

        Args:
            name (str): ユーザ名
        
        Returns: None

        Raises:
            ValueError: 同一ユーザが存在している場合
        """
        user : User = User(UserName(name))

        if self._user_service.exists(user):
            raise ValueError("ユーザはすでに存在しています")

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
            コマンドオブジェクトを利用するように変更した
            情報変更があっても引数が変化しない
        """
        target_id: UserId = UserId(user_id)
        user: Optional[User] = self._user_repository.find_by_id(target_id)

        if user is None: raise ValueError("user_idの値が不適切です")

        name: Optional[str] = command.name
        if name is not None:
            new_user_name: UserName = UserName(name)
            user.change_name(new_user_name)
            if self._user_service.exists(user):
                raise ValueError("そのユーザはすでに存在しています")

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
        """
        target_id: UserId = UserId(command.id)
        user: User = self._user_repository.find_by_id(target_id)

        # 対象が見つからなかった場合は退会成功とする
        if user is None: return

        self._user_repository.delete(user)