"""
2.4節のコードの説明
"""
from dataclasses import dataclass
from typing import Final

# リスト2.27
@dataclass
class Money:
    """
    量と通貨単位を属性にもつお金オブジェクト
    データを保持するだけではなく、振る舞いを持つこともできる

    Attributes:
        amount (float): (お金の)量
        currency (str): 通貨単位(円やドル)
    """
    amount: Final[float]
    currency: Final[str]
