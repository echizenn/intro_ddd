"""
2.4節のコードの説明
"""

# リスト2.27
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
