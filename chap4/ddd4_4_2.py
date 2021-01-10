"""
4.4.2節のコードの説明
"""
from ddd4_4_1 import User, UserName

# リスト4.11
class Program:
    """
    ユーザ作成処理の実装
    """
    def create_user(self, user_name: str):
        """
        ユーザ作成処理

        Args:
            user_name (str): ユーザ名

        Returns: None

        Raises:
            ValueError: ユーザ名が重複しているとき
        """
        user: User = User(UserName(user_name))

        user_service: UserService = UserService()
        if user_service.exists(user):
            raise ValueError("{}はすでに存在しています".format(user_name))

        # SQL接続コードをこの後書いているが
        # pythonで書き直すのは面倒+本質的でないので変数の説明のみ
        # connectionString: DBの情報
        # connection: usingを使って DBとの接続を確立
        # command: DBにする操作を{}内に記入
        # この辺、DBに対する具体的な操作が多数書かれているのを確認する。

# リスト4.12
class UserService:
    """
    ドメインサービスの実装

    Attributes: None

    Note:
        ここでもDBとの操作の操作が多いことを確認する。
    """
    def exists(self, user: User) -> bool:
        """
        userが存在しているか確認

        Args:
            user (User): 重複を確認したいユーザ
        
        Returns:
            bool: 重複しているか否か
        """
        # SQL接続コードをこの後書いているが
        # pythonで書き直すのは面倒+本質的でないので変数の説明のみ
        # connectionString: DBの情報
        # connection: usingを使って DBとの接続を確立
        # command: DBにする操作を{}内に記入
        # この辺、DBに対する具体的な操作が多数書かれているのを確認する。
        pass
