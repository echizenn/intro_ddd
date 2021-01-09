"""
2.2.2節のコードの説明
"""
from ddd2_1 import FullName

# リスト2.11
def list2_11():
    """
    普段行っている値の変更

    Args: None

    Returns: None

    Notes:
        普段行っている値の変更
    """
    # 数字の変更
    num: int = 0
    num = 1

    # 文字の変更
    c: str = '0'
    c = 'b'

    # 文字列の変更(pythonだと文字と文字列は同じ)
    greet: str = "こんにちは"
    greet = "hello"

# リスト2.12
def list2_12():
    """
    値オブジェクトの変更方法

    Args: None

    Returns: None

    Notes:
        値オブジェクトで値の変更をするときのやり方
        変更ではなく、代入による交換をするしかない
    """
    full_name: FullName = FullName("masanobu", "naruse")
    full_name = FullName("masanobu", "sato")
