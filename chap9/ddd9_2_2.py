"""
9.2.2節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Final

import pyodbc

from chap4.ddd4_4_1 import User, UserId, UserName

# リスト9.10
class IUserRepository(metaclasss=ABCMeta):
    """
    リポジトリに採番処理を定義する
    """
    @abstractmethod
    def find(self, id: UserId) -> User:
        pass

    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def next_identity(self) -> UserId:
        pass

# リスト9.11
@dataclasses.dataclass
class UserApplicationService:
    """
    採番処理を利用してユーザを登録する
    """
    _user_repository: Final[IUserRepository]

    def register(self, command: UserRegisterCommand):
        user_name = UserName(command.name)
        user = User(self._user_repository.next_identity(), user_name)
        pass

# リスト9.12
@dataclasses.dataclass
class UserRepository(IUserRepository):
    """
    採番処理と永続化で利用される技術が異なる
    """
    _numbering_api: Final[NumberingApi]

    # リレーショナルデータベースを利用しているが
    def find(self, id: UserId) -> User:
        connection_string: str = "DRIVER={SQL Server};SERVER=" \
            + instance + ";uid=" + user + ";pwd=" + pasword + ";DATABASE=" + db
        with pyodbc.connect(connection_string) as connection:
            cursor = connection.cursor()
            command_text: str = """SELECT name FROM users WHERE id = @id"""
            cursor.execute(command_text, id.value)
            row = cursor.fetchone()
            connection.commit()
        name = str(row[0]) # これで動くと思うが、コードを動かしての確認まではしていない
        return User(id, UserName(name))   

    # 採番処理はリレーショナルデータベースを利用していない
    def next_identity(self) -> UserId:
        response = self._numbering_api.request()
        return UserId(response.next_id)