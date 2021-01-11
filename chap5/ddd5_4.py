"""
5.4節のコードの解説
"""
from typing import Optional

import pyodbc

from ddd5_2_2 import Program
from ddd5_3_1 import IUserRepository

# リスト5.10, 5.11
class UserRepository(IUserRepository):
    """
    SQLを利用したレポジトリ
    pyodbcモジュール使うとさまざまなDBと接続できそうなので、
    pyodbcモジュールを使うと仮定して書く。
    """
    def __init__(self):
        instance = "インスタンス"
        user = "ユーザー"
        pasword = "パスワード"
        db = "Sample"

        self._connection_string: str = "DRIVER={SQL Server};SERVER=" \
            + instance + ";uid=" + user + ";pwd=" + pasword + ";DATABASE=" + db

    def save(self, user: User):
        """
        重複を確認して保存する

        Args:
            user (User): 保存したいUserインスタンス
        
        Returns: None
        """
        # C#のusingはpythonのwithにあたるはず(厳密には違うが)
        # この関数内は本との対応関係崩れます
        with pyodbc.connect(self._connection_string) as connection:
            cursor = connection.cursor()
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
            connection.commit()

    def find(self, user_name: UserName) -> Optional[User]:
        """
        ユーザ名からユーザを探す

        Args:
            user_name (UserName): 探したいユーザ名
        
        Returns:
            Optional[User]: ユーザが存在する場合はUserインスタンスを返す、
                            存在しない場合はNoneを返す

        Note:
            saveメソッドと同様、本との対応が若干崩れます
        """
        with pyodbc.connect(self._connection_string) as connection:
            cursor = connection.cursor()
            command_text: str = "SELECT * FROM users WHERE name = ?"

            # 第二パラメータ以降の変数が、?の部分に代入される
            cursor.execute(command_text, user_name.value)
            reader = cursor.fetchone() # SQL実行結果一行取得、ない場合はNoneが返る

            if reader:
                id: str = reader.id
                name: str = reader.name

                return User(UserId(id), UserName(name))
            else:
                return None

# リスト5.12
def list5_12():
    """
    リポジトリをProgramクラスに引き渡す

    Args: None

    Returns: None
    """
    user_repository: UserRepository = UserRepository()
    program: Program = Program(user_repository)
    program.create_user("naruse")