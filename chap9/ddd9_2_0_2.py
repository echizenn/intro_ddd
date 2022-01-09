"""
9.2節のコードの説明
"""
import dataclasses
from typing import Final, Optional

import pyodbc

from chap4.ddd4_4_1 import UserId, UserName

# リスト9.2
class User():
    """
    採番テーブルを利用するように変更

    Attributes:
        id (UserId): ユーザid
        name (UserName): ユーザ名
    """
    def __init__(self, name: UserName, id: Optional[int]=None):
        # ConfigureManagerを使わずベタうちした場合
        connection_string: str = "DRIVER={SQL Server};SERVER=" \
            + instance + ";uid=" + user + ";pwd=" + pasword + ";DATABASE=" + db
        with pyodbc.connect(self._connection_string) as connection:
            cursor = connection.cursor()
            command_text: str = """SELECT seq = (NEXT VALUE FOR UserSeq)"""
            cursor.execute(command_text)
            row = cursor.fetchone()
            connection.commit()
        seq_id = str(row[0]) # これで動くと思うが、コードを動かしての確認まではしていない
        self.id: Final[UserId] = dataclasses.field(default=seq_id, init=False) if id is None else id
        self.name: Final[UserName] = name