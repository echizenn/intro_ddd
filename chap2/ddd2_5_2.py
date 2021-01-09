"""
2.5.2節のコードの説明
"""
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
        ValueError: ユーザ名が3文字未満のとき
    """
    if len(user_name) >= 3:
        # 正常な値なので処理を継続する
        pass
    else:
        raise ValueError("異常な値です")

# リスト2.38
class UserName:
    """
    ユーザ名を表す値オブジェクト

    Attributes:
        value (str): ユーザ名の値
        
    Raises:
        ValueError: ユーザ名が3文字未満のとき

    Note:
        ガード節によって不正な値の存在を考える必要がなくなる
    """
    def __init__(self, value: str):
        # ガード節
        if len(value) < 3: raise ValueError("ユーザ名は3文字以上です。")

        self.value: Final[str] = value