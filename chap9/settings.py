"""
設定ファイル
"""
from collections import namedtuple


_instance = "インスタンス"
_user = "ユーザー"
_password = "パスワード"
_db = "Sample"

Connection = namedtuple("Connection", ["connection_string",])

CONNECTION_STRINGS = {
    "default_connection": Connection("DRIVER={SQL Server};SERVER=" + _instance \
            + ";uid=" + _user + ";pwd=" + _password + ";DATABASE=" + _db)
}