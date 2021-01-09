"""
2.5.1節のコードの説明
"""
from dataclasses import dataclass
from typing import Final, NamedTuple

# リスト2.33
def list2_33():
    """
    プリミティブな値を利用した製品番号

    Args: None

    Returns: None

    Note:
        プリミティブな値を利用するとmodel_numberの内容がわからない
    """
    model_number: str = "a20421-100-1"

# リスト2.34
def list2_34(model_number: str): # かろうじて文字列であることはわかる
    """
    製品番号はどういったものだろうか

    Args:
        model_number (str): 製品番号

    Returns: None

    Note:
        model_numberを利用したメソッド
    """
    pass

# リスト2.35
class ModelNumber(NamedTuple):
    """
    製品番号を表す値オブジェクト

    Attributes:
        _product_code (str): プロダクトコード
        _branch (str): 枝番
        _lot (str): ロット番号
    """
    _product_code: Final[str]
    _branch: Final[str]
    _lot: Final[str]

    def __str__(self) -> str:
        return self.product_code + "-" + self.branch + "-" + self.lot
