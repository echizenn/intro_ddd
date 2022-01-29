"""
6.5節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses

# リスト6.35
class IUserRegisterService(metaclass=ABCMeta):
    """
    ユーザ登録処理のインターフェース

    Attributes: None
    """
    @abstractmethod
    def handle(self, command: UserRegisterCommand):
        """
        実行

        Args:
            command (UserRegisterCommand): 登録したいユーザ
        
        Returns: None
        """
        pass


# リスト6.36
@dataclasses.dataclass
class Client:
    """
    クライアントはインターフェースを利用する

    Attributes:
        _user_repository_service (IUserRegisterService): ユーザーレポジトリサービス
    """
    _user_repository_service: IUserRegisterService

    def register(self, name: str):
        """
        ユーザ登録処理

        Args:
            name (str): ユーザ名
        
        Returns: None
        """
        command = UserRegisterCommand(name)
        self._user_repository_service.handle(command)


# リスト6.37
class MockUserRegisterService(IUserRegisterService):
    """
    ユーザ登録処理のインターフェース

    Attributes: None
    """
    @abstractmethod
    def handle(self, command: UserRegisterCommand):
        """
        実行

        Args:
            command (UserRegisterCommand): 登録したいユーザ
        
        Returns: None
        """
        pass

# リスト6.38
class ExceptionUserRegisterService(IUserRegisterService):
    """
    例外を送出させるモックオブジェクト

    Attributes: None
    """
    @abstractmethod
    def handle(self, command: UserRegisterCommand):
        """
        実行

        Args:
            command (UserRegisterCommand): 登録したいユーザ
        
        Returns: None

        Raises:
            ComplexException: 例外
        """
        raise ComplexExeption()
