"""
9.2節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Final
from chap5.ddd5_3_1 import IUserRepository

import pyodbc

from chap4.ddd4_4_1 import UserId, UserName

# リスト9.3
class IUserFactory(metaclasss=ABCMeta):
    """
    ファクトリのインターフェース
    """
    @abstractmethod
    def create(self, name: UserName):
        pass

# リスト9.4
class UserFactory(IUserFactory):
    """
    シーケンスを利用したファクトリ
    """
    def create(self, name: UserName):
        connection_string: str = "DRIVER={SQL Server};SERVER=" \
            + instance + ";uid=" + user + ";pwd=" + pasword + ";DATABASE=" + db
        with pyodbc.connect(connection_string) as connection:
            cursor = connection.cursor()
            command_text: str = """SELECT seq = (NEXT VALUE FOR UserSeq)"""
            cursor.execute(command_text)
            row = cursor.fetchone()
            connection.commit()
        seq_id = str(row[0]) # これで動くと思うが、コードを動かしての確認まではしていない
        id = UserId(seq_id)
        return User(id, name)

# リスト9.5
@dataclasses.dataclass
class User():
    """
    Userクラスのコンストラクタはひとつになる

    Attributes:
        id (UserId): ユーザid
        name (UserName): ユーザ名
    """
    id: Final[UserId]
    name: Final[UserName]

# リスト9.6
@dataclasses.dataclass
class UserApplicationService():
    """
    ファクトリを経由してインスタンスを生成する
    """
    _user_factory: Final[IUserFactory]
    _user_repository: Final[IUserRepository]
    _user_service: Final[UserService]

    def register(self, command: UserRegisterCommand):
        user_name = UserName(command.name)
        # ファクトリによってインスタンスを生成する
        user = self._user_factory.create(user_name)

        if self._user_service.exists(user):
            raise ValueError("そのユーザはすでに存在しています")
        self._user_repository.save(user)

# リスト9.7
@dataclasses.dataclass
class InMemoryUserFactory(IUserFactory):
    """
    インメモリで動作するファクトリ"""
    current_id: Final[int]

    def create(self, name: UserName) -> User:
        self.current_id += 1
        return User(UserId(str(self.current_id)), name)