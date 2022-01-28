"""
2.4節のコードの説明
"""
from __future__ import annotations # これで自己クラスを型ヒントで使える
import dataclasses
from typing import Final

# リスト2.28
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

    def __add__(self, arg: Money) -> Money:
        """
        お金の加算操作、通貨単位が異なるとエラーが出る

        Args:
            arg (Money): 加算したいお金
        
        Returns:
            Money: 加算結果のお金

        Raises:
            ValueError: 通貨単位が異なる和算をしているとき
               
        Note:
            pythonは+演算子を実行すると、__add__メソッドを呼ぶ
            private変数は同一クラスなら呼べるのでarg._currencyで問題ない
        """
        if self._currency != arg._currency:
            raise ValueError("通貨単位が異なります" \
                    f"(self:{self._currenc}, arg:{arg._currency})")
        
        return Money(self.amount + arg.amount, self._currency)

# リスト2.29
def list2_29():
    """
    加算した結果を受け取る

    Args: None

    Returns: None

    Notes:
        +演算子では、__add__メソッドが呼び出される
        加算が行えていることが確認できる。
    """
    my_money: Money = Money(1000, "JPY")
    allowance: Money = Money(3000, "JPY")
    result: Money = my_money + allowance

 # リスト2.30
def list2_30():
    """
    プリミティブな値(小数型)同士の加算

    Args: None

    Returns: None

    Note:
        同じ操作をしていることを確認する。
    """
    my_money: float = 1000
    allowance: float = 3000
    result: float = my_money + allowance

# リスト2.31
def list2_31():
    """
    異なる通貨単位同士で加算は例外を送出する

    Args: None

    Returns: None

    Note:
        値オブジェクトを利用することで誤操作を防ぎやすくなる。
    """
    jpy: Money = Money(1000, "JPY")
    usd: Money = Money(10, "USD")
    result: Money = jpy + usd