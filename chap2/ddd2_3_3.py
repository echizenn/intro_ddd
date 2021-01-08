"""
2.3節のコードの説明
"""

# リスト2.25
class Name:
    """
    名前を表現するクラス

    Attributes:
        value (str): 名前、アルファベットのみで構成される
    """
    def __init__(self, value: str):
        if not value: raise ValueError("valueが定義されていません")
        if not re.fullmatch('[a-zA-Z]+', value):
            raise ValueError("許可されていない文字が使われています")
        
        self.value: str = value

# リスト2.26
class FullName:
    """
    リスト2.25のNameクラスを利用したFullNameクラス

    Attributes:
        first_name (Name): 名
        last_name (Name): 姓
    """
    def __init__(self, first_name: Name, last_name: Name):
        if not first_name: raise ValueError("first_nameが定義されていません")
        if not last_name: raise ValueError("last_nameが定義されていません")

        self.first_name: Name = first_name
        self.last_name: Name = last_name
