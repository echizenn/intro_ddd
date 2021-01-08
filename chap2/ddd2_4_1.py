"""
2.4.1節のコードの説明
"""
from __future__ import annotations # これで自己クラスを型ヒントで使える

# リスト2.32
class Money:
    """
    量と通貨単位を属性にもつお金オブジェクト
    データを保持するだけではなく、振る舞いを持つこともできる

    Attributes:
        amount (float): (お金の)量
        currency (str): 通貨単位(円やドル)
    """
    def __init__(self, amount: float, currency: str):
        if not currency: raise ValueError("currencyが定義されていません")

        self.amount: float = amount
        self.currency: str = currency

    def __add__(self, arg: Money) -> Money:
        """
        お金の加算操作、通貨単位が異なるとエラーが出る

        Args:
            arg (Money): 加算したいお金
        
        Returns:
            Money: 加算結果のお金
        
        Note:
            pythonは+演算子を実行すると、__add__メソッドを呼ぶ
        """
        if not arg: raise ValueError("currencyが定義されていません")
        if self.currency != arg.currency:
            raise ValueError("通貨単位が異なります" \
                    "(self:{}, arg:{})".format(self.currency, arg.currency))
        
        return Money(self.amount + arg.amount, self.currency)

    def multiply(self, rate: Rate):
        """
        お金を乗算するふるまい
        
        Args:
            rate (Rate): 金利(実装はしていない)
        
        Retunrs:
            Money: 金利を考えたお金
        
        Note:
            仮想的な関数で中身は実装していません
        """
        pass