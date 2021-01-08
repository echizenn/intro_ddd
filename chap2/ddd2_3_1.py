"""
2.3節のコードの説明
"""
from dataclasses import dataclass

# リスト2.21
@dataclass
class FullName:
    """
    可能な限り値オブジェクトを適用したFullNameクラス

    Attributes:
        first_name (FirstName): 名を表すオブジェクト
        last_name (LastName): 姓を表すオブジェクト
    """
    first_name: FirstName
    last_name: LastName

# リスト2.22
class FirstName:
    """
    名を表す値オブジェクト

    Attributes:
        value (str): 名前
    """
    def __init__(self, value: str):
        if not value: raise ValueError("1文字以上である必要があります。")
        self.value = value

# リスト2.23
class LastName:
    """
    姓を表す値オブジェクト

    Attributes:
        value (str): 姓
    """
    def __init__(self, value: str):
        if not value: raise ValueError("1文字以上である必要があります。")
        self.value = value
