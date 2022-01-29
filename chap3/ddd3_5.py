"""
3.5節のコードの説明
"""

# リスト3.8
class User:
    """
    無口なコード
    ここでの目的上説明用のdocsはこれ以上書きません

    Note:
        ユーザ名が文字列ということしかわからない
    """
    def __init__(self, name: str):
        self.name: str = name

# リスト3.9
class UserName:
    """
    饒舌なコード

    Attributes:
        _value (str): ユーザ名

    Raises:
        ArgumentException: ユーザ名が3文字未満のとき

    Note:
        ユーザ名が3文字以上でなければ動作しないことはコードだけ見てもわかる
    """
    def __init__(self, value: str):
        if len(value) < 3: raise ArgumentException("ユーザ名は3文字以上です", str(value))

        self._value = value