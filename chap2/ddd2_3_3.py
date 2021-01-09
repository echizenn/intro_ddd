"""
2.3節のコードの説明
"""
from dataclasses import dataclass
from typing import Final

# リスト2.25
class Name:
    """
    名前を表現するクラス

    Attributes:
        value (str): 名前、アルファベットのみで構成される

    Raises:
        ValueError: アルファベット以外が名前として使われているとき
    """
    def __init__(self, value: str):
        if not value: raise ValueError("valueが定義されていません")
        if not re.fullmatch('[a-zA-Z]+', value):
            raise ValueError("許可されていない文字が使われています")
        
        self.value: Final[str] = value

# リスト2.26
@dataclass
class FullName:
    """
    リスト2.25のNameクラスを利用したFullNameクラス

    Attributes:
        first_name (Name): 名
        last_name (Name): 姓
    """
    first_name: Final[Name]
    last_name: Final[Name]
