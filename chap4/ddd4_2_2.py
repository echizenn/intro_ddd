"""
4.2.2節のコードの説明
"""

from chap2.ddd2_5_3 import UserId, UserName
from ddd4_2_1 import User


# リスト4.4
class UserService:
    """
    ユーザのドメインサービスの定義
    自身のふるまいを変更するようなインスタンス特有の状態をもたないオブジェクトになっている

    Attributes: None
    """
    
    def exists(user: User) -> bool:
        """
        重複を確認する

        Args:
            user (User): 確認したいユーザ
        
        Returns:
            bool: 重複しているか否か
        
        Note:
            実装はしません
        """
        pass

# リスト4.5
def list4_5():
    """
    リスト4.4を利用して重複確認を行う

    Args: None

    Returns: None

    Note:
        不自然さがなくなるのを確認
    """
    user_service: UserService = UserService()

    user_id: UserId = UserId("id")
    user_name: UserName = UserName("naruse")
    user: User = User(user_id, user_name)

    # ドメインサービスに問い合わせ
    duplicate_check_result: bool = user_service.exists(user)
    print(duplicate_check_result)