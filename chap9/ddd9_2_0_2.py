"""
9.2節のコードの説明
"""
import dataclasses
from typing import Final, Optional

import pyodbc

from chap4.ddd4_4_1 import UserId, UserName
import settings

# リスト9.2
class User():
    """
    採番テーブルを利用するように変更

    Attributes:
        id (UserId): ユーザid
        name (UserName): ユーザ名
    """
    def __init__(self, name: UserName, id: Optional[int]=None):
        connection_string: str = settings.CONNECTION_STRINGS["default_connection"].connection_string
        with pyodbc.connect(connection_string) as connection:
            cursor = connection.cursor()
            command_text: str = """SELECT seq = (NEXT VALUE FOR UserSeq)"""
            cursor.execute(command_text)
            row = cursor.fetchone()
            connection.commit()
        seq_id = str(row[0]) # これで動くと思うが、コードを動かしての確認まではしていない
        self.id: Final[UserId] = dataclasses.field(default=seq_id, init=False) if id is None else id
        self.name: Final[UserName] = name