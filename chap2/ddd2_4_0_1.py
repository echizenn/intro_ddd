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
        _amount (float): (お金の)量
        _currency (str): 通貨単位(円やドル)
    """
    _amount: Final[float]
    _currency: Final[str]

    @property
    def amount(self) -> float:
        """
        外部からamountを取得できるようにする

        Args: None

        Returns:
            float: お金の量
        """
        return self._amount
    
    @property
    def currency(self)-> str:
        """
        外部からcurrencyを取得できるようにする

        Args: None

        Returns:
            str: 通貨単位(円やドル)
        """
        return self._currency
