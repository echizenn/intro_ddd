"""
2.5.1節のコードの説明
"""
from dataclasses import dataclass
from typing import Final

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
@dataclass
class ModelNumber:
    """
    製品番号を表す値オブジェクト

    Attributes:
        product_code (str): プロダクトコード
        branch (str): 枝番
        lot (str): ロット番号
    """
    product_code: Final[str]
    branch: Final[str]
    lot: Final[str]

    def __str__(self) -> str:
        return self.product_code + "-" + self.branch + "-" + self.lot