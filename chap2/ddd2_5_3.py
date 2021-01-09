"""
2.5.3節のコードの説明
"""
from dataclasses import dataclass
from typing import Final

# リスト2.39,43
def create_user(name: str) -> User:
    """
    単純な代入を行うコード

    Args:
        name (str): ユーザ名
    
    Returns:
        User: ユーザ名nameであるユーザ

    Note:
        (静的型付け言語なら)型が合わないのでエラーが出る
        そもそもUserクラス実装していないので動かないです
    """
    user: User = User()
    user.id = name # コンパイルエラー(mypyを使うとpythonでもエラー出してくれる)
    return user

# リスト2.40
@dataclass
class UserId:
    """
    ユーザIDの値オブジェクト

    Attributes:
        value (str): ユーザID
    """
    value: Final[str]

# リスト2.41
@dataclass
class UserName:
    """
    ユーザ名の値オブジェクト

    Attributes:
        value (str): ユーザ名
    """
    value: Final[str]

# リスト2.42
@dataclass
class User:
    """
    値オブジェクトを利用するように変更したUserクラス

    Attributes:
        id (UserId): ユーザIDの値オブジェクト
        name (UserName): ユーザ名の値オブジェクト
    """
    # 初期値がないとpythonだとUser()でエラーが出るので初期値入力した
    id: UserId = UserId("1")
    name: UserName = UserName("masanobu")
    