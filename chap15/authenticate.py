"""
15.4節のコードの説明
"""

# pythonはファイル変えれば問題ない
# リスト15.6
class User:
    """
    別のオブジェクトとして定義する
    """
    def __init__(self, id: UserId, password: Password):
        if id is None: raise ArgumentNullException(id)
        if password is None: raise ArgumentNullException(password)

        self._id = id
        self._password = password

    def id(self) -> UserId:
        return self._id
    
    def is_same_password(self, password: Password) -> bool:
        return self._password == password