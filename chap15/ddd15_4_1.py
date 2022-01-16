"""
15.4節のコードの説明
"""

# リスト15.5
class User:
    """
    パスワードの認証ができるようにメソッドを追加する
    """
    def __init__(self, id: UserId, name: UserName, password: Password):
        if id is None: raise ArgumentNullException(id)
        if name is None: raise ArgumentNullException(name)
        if password is None: raise ArgumentNullException(password)

        self._id = id
        self._name = name
        self._password = password

    def id(self) -> UserId:
        return self._id
    
    def change_name(self, name: UserName):
        if name is None: raise ArgumentNullException(id)

        self._name = name

    def is_same_password(self, password: Password) -> bool:
        return self._password == password
