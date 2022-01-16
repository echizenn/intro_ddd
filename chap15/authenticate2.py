"""
15.5節のコードの説明
"""

# リスト15.7
class User:
    """
    ユーザ名を識別子とする
    """
    def __init__(self, id: UserName, password: Password):
        if id is None: raise ArgumentNullException(id)
        if password is None: raise ArgumentNullException(password)

        self._id = id
        self._password = password

    def id(self) -> UserName:
        return self._id
    
    def is_same_password(self, password: Password) -> bool:
        return self._password == password