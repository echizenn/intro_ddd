"""
15.5節のコードの説明
"""

# リスト15.8
class User:
    """
    Coreパッケージも変更しなくてはいけないはずが
    """
    # 識別子はUserIdのままである
    def __init__(self, id: UserId, name: UserName):
        if id is None: raise ArgumentNullException(id)
        if name is None: raise ArgumentNullException(name)

        self._id = id
        self._name = name

    def id(self) -> UserId:
        return self._id
    
    # 識別子となったUserNameが変更できてしまう
    def change_name(self, name: UserName):
        if name is None: raise ArgumentNullException(id)

        self._name = name