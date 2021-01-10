"""
4.2.1節のコードの説明
"""
from typing import Final

# リスト4.1
class User:
    """
    重複確認のふるまいをUserクラスに追加

    Attributes:
        _id (UserId): ユーザid
        _name (UserName): ユーザ名

    Note:
        UserIdとUserNameクラスimportしていないので動きません
    """
    def __init__(self, id: UserId, name: UserName):
        self._id: Final[UserId] = id
        self._name: UserName = name

    def exists(self, user: User):
        """
        重複を確認するコード

        Args:
            user (User): 確認したいユーザ
        
        Returns:
            bool: 重複しているか否か
        
        Note:
            実装はしません
        """
        pass

# リスト4.2
def list4_2():
    """
    リスト4.1を利用して重複確認を行う

    Args: None

    Returns: None

    Note:
        自身が重複かを自身に尋ねるのは違和感がある
    """
    user_id: UserId = UserId("id")
    user_name: UserName = UserName("nrs")
    user: User = User(user_id, user_name)

    # 生成したオブジェクト自身に問い合わせることになる
    duplicate_check_result: bool = user.exists(user)
    print(duplicate_check_result) # True? False?

# リスト4.3
def list4_3():
    """
    重複確認専用のインスタンスを用意する

    Args: None

    Returns: None

    Note:
        自身に問い合わせない点では不自然ではなくなったが、
        check_objectはユーザを表すがユーザではない不自然なオブジェクトになる
    """
    check_id: UserId = UserId("check")
    check_name: UserName = UserName("checker")
    check_object: User = User(check_id, check_name)

    user_id: UserId = UserId("id")
    user_name: UserName = UserName("nrs")
    user: User = User(user_id, user_name)

    # 重複確認専用インスタンスに問い合わせ
    duplicate_check_result: bool = check_object.exists(user)
    print(duplicate_check_result)
