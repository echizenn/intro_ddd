"""
4.3節のコードの説明
"""

#  リスト4.8
class User:
    """
    Userクラスにふるまいを定義する

    Attributes:
        _id (UserId): ユーザid
        _name (UserName): ユーザ名

    Note:
        饒舌なUserクラスになっている
    """
    def __init__(self, id: UserId, name: UserName):
        self._id: UserId = id
        self._name: UserName = name

    def change_user_name(self, name: UserName):
        self._name = name