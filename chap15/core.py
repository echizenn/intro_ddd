"""
15.4節のコードの説明
"""

# pythonはファイル変えれば問題ない
# リスト15.6
class User:
    """
    別のオブジェクトとして定義する
    """
    def __init__(self, id: UserId, name: UserName):
        if id is None: raise ArgumentNullException(id)
        if name is None: raise ArgumentNullException(name)

        self._id = id
        self._name = name

    def id(self) -> UserId:
        return self._id
    
    def change_name(self, name: UserName):
        if name is None: raise ArgumentNullException(id)

        self._name = name