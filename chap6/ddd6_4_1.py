"""
6.4.1節のコードの説明
"""
import dataclasses
from typing import Final
from ddd6_2_1 import IUserRepository, User, UserName, UserId

# リスト6.32
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

    def register(self, command: UserRegisterCommand):
        """
        ユーザ登録処理

        Args:
            name (str): ユーザ名
        
        Returns: None

        Raises:
            ValueError: 同一ユーザが存在している場合
        """
        user = User(UserName(command.name))

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
        target_id = UserId(user_id)
        user = self._user_repository.find_by_id(target_id)

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
        target_id = UserId(command.id)
        user = self._user_repository.find_by_id(target_id)

        if user is None: raise ValueError("user_idの値が不適切です")

        name: Optional[str] = command.name
        if name is not None:
            new_user_name = UserName(name)
            user.change_name(new_user_name)
            if self._user_service.exists(user):
                raise ValueError("そのユーザはすでに存在しています")

        mail_address: Optional[str] = command.mail_address
        if mail_address is not None:
            new_mail_address: MailAddress = MailAddress(mail_address)
            user.change_mail_address(new_mail_address)
        
        self._user_repository.save(user)

    def delete(command: UserDeleteCommand):
        """
        退会処理

        Args:
            command (UserUpdateCommand): 退会したいユーザのコマンドオブジェクト

        Returns: None

        Raises:
            ValueError: 存在しないユーザのuser_idの場合
        """
        target_id = UserId(command.id)
        user = self._user_repository.find_by_id(target_id)

        if user is None: raise ValueError("user_idの値が不適切です")

        self._user_repository.delete(user)


# リスト6.33
@dataclasses.dataclass
class UserRegisterService:
    """
    ユーザ登録処理クラス

    Attributes:
        _user_repository (IUserRepository): ユーザのレポジトリ
        _user_service (UserService): ユーザのドメインサービス
    """
    _user_repository: Final[IUserRepository]
    _user_service: Final[UserService]

    def handle(self, command: UserRegisterCommand):
        """
        実行

        Args:
            command (UserRegisterCommand): 登録したいユーザ
        
        Returns: None
        """
        user_name = UserName(command.name)

        user = User(user_name)

        if self._user_service.exists(user):
            raise ValueError("ユーザはすでに存在しています")

        self._user_repository.save(user)
        

# リスト6.34
@dataclasses.dataclass
class UserDeleteService:
    """
    ユーザ退会処理クラス

    Attributes:
        _user_repository (IUserRepository): ユーザのレポジトリ
    """
    _user_repository: Final[IUserRepository]

    def handle(command: UserDeleteCommand):
        """
        退会処理

        Args:
            command (UserUpdateCommand): 退会したいユーザのコマンドオブジェクト

        Returns: None

        Raises:
            ValueError: 存在しないユーザのuser_idの場合
        """
        user_id = UserId(command.id)
        user = self._user_repository.find_by_id(user_id)

        if user is None: raise ValueError("user_idの値が不適切です")

        self._user_repository.delete(user)