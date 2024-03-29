"""
2.5.2節のコードの説明
"""
import dataclasses
from typing import Final

# リスト2.36
def list2_36():
    """
    存在してはいけない値

    Args: None

    Returns: None

    Note:
        「ユーザ名は3文字以上」というルールが存在している
    """
    user_name: str = "me"

# リスト2.37
def list2_37(user_name: str):
    """
    値を利用する前にルールに照らし合わせる必要がある

    Args:
        user_name (str): ユーザ名
    
    Returns: None

    Raises:
        Exception: ユーザ名が3文字未満のとき
    """
    if len(user_name) >= 3:
        # 正常な値なので処理を継続する
        pass
    else:
        raise Exception("異常な値です")

# リスト2.38
@dataclasses.dataclass(frozen=True)
class UserName:
    """
    ユーザ名を表す値オブジェクト

    Attributes:
        _value (str): ユーザ名の値
        
    Raises:
        ArgumentException: ユーザ名が3文字未満のとき

    Note:
        ガード節によって不正な値の存在を考える必要がなくなる
    """
    _value: Final[str]

    def __post_init__(self):
        # ガード節
        if len(self._value) < 3: raise ArgumentException("ユーザ名は3文字以上です。", str(self._value))