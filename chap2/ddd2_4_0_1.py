"""
2.4節のコードの説明
"""
import dataclasses
from typing import Final

# リスト2.27
@dataclasses.dataclass
class Money:
    """
    量と通貨単位を属性にもつお金オブジェクト
    データを保持するだけではなく、振る舞いを持つこともできる

    Attributes:
        _amount (float): (お金の)量
        _currency (str): 通貨単位(円やドル)
    """
    _amount: Final[float]
    _currency: Final[str]
