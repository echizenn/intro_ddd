"""
6.2.4節のコードの説明
"""
import dataclasses
from typing import Final, Optional

from ddd6_2_1 import IUserRepository, UserService, User, UserName, UserId

# リスト6.17(Pythonだと本の前者の書き方はできないと思う)
class UserUpdateCommand:
    """
    コマンドオブジェクト

    Attributes:
        _id (str): ユーザid
        _name (str): ユーザ名
        _mail_address (str): メールアドレス
    """
    _id: str
    _name: Optional[str] = None
    _mail_address: Optional[str] = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def mail_address(self) -> Optional[str]:
        return self._mail_address

# リスト6.18
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

    def register(self, name: str):
        """
        ユーザ登録

        Args:
            name (str): ユーザ名
        
        Returns: None

        Raises:
            CanNotRegisterUserException: 同一ユーザが存在している場合
        """
        user : User = User(UserName(name))

        if self._user_service.exists(user):
            raise CanNotRegisterUserException(user, "ユーザはすでに存在しています")

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
            UserNotFoundException: 存在しないユーザのidを指定した場合
            CanNotRegisterUserException: 同一ユーザが存在している場合

        Note:
            コマンドオブジェクトを利用するように変更した
            情報変更があっても引数が変化しない
        """
        target_id: UserId = UserId(command.id)
        user: Optional[User] = self._user_repository.find_by_id(target_id)

        if user is None: raise UserNotFoundException(target_id)

        name: Optional[str] = command.name
        if name is not None:
            new_user_name: UserName = UserName(name)
            user.change_name(new_user_name)
            if self._user_service.exists(user):
                raise CanNotRegisterUserException(user, "ユーザはすでに存在しています")

        mail_address: Optional[str] = command.mail_address
        if mail_address is not None:
            new_mail_address: MailAddress = MailAddress(mail_address)
            user.change_mail_address(new_mail_address)
        
        self._user_repository.save(user)
        
# リスト6.19
def list6_19(id: str, user_application_service: UserApplicationService):
    """
    コマンドオブジェクトを利用してアプリケーションサービスの制御を行う

    Args:
        id (str): ユーザid
        user_application_service (UserApplicationService):
                                                    ユーザアプリケーションサービス

    Returns: None
    """
    update_name_command: UserUpdateCommand = UserUpdateCommand(id,
                                                                _name="naruse")
    user_application_service.update(update_name_command)

    # メールアドレス変更だけを行うように
    updaet_mail_command: UserUpdateCommand = UserUpdateCommand(id,
                                            _mail_address="xxxx@example.com")