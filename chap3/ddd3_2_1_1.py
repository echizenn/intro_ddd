"""
3.2.1節のコードの説明
"""

# リスト3.1
class User:
    """
    ユーザを表すクラス

    Attributes:
        _name (str): ユーザ名

    Raises:
        ValueError: ユーザ名が3文字未満のとき
    """
    def __init__(self, name: str):
        if len(name) < 3: raise ValueError("ユーザ名は3文字以上です。")

        self._name: Final[str] = name
