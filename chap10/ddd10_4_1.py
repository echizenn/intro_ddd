"""
10.4.1節のコードの説明
"""
import dataclasses
from typing import Final, Optional

import pyodbc

from chap4.ddd4_4_1 import User, UserName
from chap9.ddd9_2_0_3 import IUserFactory
from chap9.ddd9_2_2 import IUserRepository
from chap10.ddd10_3_2 import UserService

# pyodbcはデフォルトでトランザクション処理をしているらしく
# 10.4.1のようなコードの書き方はできなさそうだが、
# できると仮定して書く

# リスト10.4
@dataclasses.dataclass
class UserRepository(IUserRepository):
    _connection: Final[SqlConnection]

    def save(self, user: User, transaction: Optional[SqlTransaction]=None):
        with pyodbc.connect(self._connection_string) as connection:
            cursor = connection.cursor()
            if transaction is not None:
                cursor.transaction = transaction # これは現実では動かない
            command_text: str = """MERGE INTO users
                USING( SELECT ? AS id, ? AS name ) AS data
                ON users.id = data.id
                WHEN MATCHED THEN
                    UPDATE SET name = data.name
                WHEN NOT MATCHED THEN
                    INSERT (id, name)
                    VALUES (data.id, data.name)"""

            # 第二パラメータ以降の変数が、?の部分に代入される
            cursor.execute(command_text, user.id.value, user.name.value)
            connection.commit() # ここでpyodbc側でトランザクションをチェックしているっぽい

# リスト10.5
# リスト10.6
@dataclasses.dataclass
class UserApplicationService:
    """
    コンストラクタでトランザクションを受け取る
    """
    _connection: Final[SqlConnection]
    _user_service: Final[UserService]
    _user_factory: Final[IUserFactory]
    _user_repository: Final[IUserRepository]

    def register(self, command: UserRegisterCommand):
        """
        トランザクションを利用するようにユーザ登録処理を書き換える
        """
        # コネクションからトランザクションを開始
        with pyodbc.connect(self._connection_string) as connection:
            transaction = connection.begin_transaction() # このようなコマンドがあると仮定する
            user_name = UserName(command.name)
            user = self._user_factory.create(user_name)
            
            if self._user_service.exists(user):
                raise ValueError("ユーザはすでに存在しています。")
            
            self._user_repository.save(user, transaction)
            # 完了時にコミットを行う
            transaction.commit() # このようなコマンドがあると仮定する