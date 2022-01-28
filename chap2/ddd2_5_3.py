"""
2.5.3節のコードの説明
"""
import dataclasses
from typing import Final

# リスト2.40
@dataclasses.dataclass(frozen=True)
class UserId:
    """
    ユーザIDの値オブジェクト

    Attributes:
        _value (str): ユーザID
    """
    _value: Final[str]

# リスト2.41
@dataclasses.dataclass(frozen=True)
class UserName:
    """
    ユーザ名の値オブジェクト

    Attributes:
        _value (str): ユーザ名
    """
    _value: Final[str]

# リスト2.42
@dataclasses.dataclass(frozen=True)
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
    