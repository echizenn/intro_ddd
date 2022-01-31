"""
5.2節のコードの説明
"""

from chap4.ddd4_4_1 import User, UserName

# リスト5.1
class Program:
    """
    第4章で登場したユーザ作成処理の実装
    """
    def create_user(self, user_name: str):
        """
        ユーザ作成処理

        Args:
            user_name (str): ユーザ名

        Returns: None

        Raises:
            Exception: ユーザ名が重複しているとき
        """
        user: User = User(UserName(user_name))

        user_service: UserService = UserService()
        if user_service.exists(user):
            raise Exception(f"{user_name}はすでに存在しています")

        # SQL接続コードをこの後書いているが
        # pythonで書き直すのは面倒+本質的でないので変数の説明のみ
        # connectionString: DBの情報
        # connection: usingを使って DBとの接続を確立
        # command: DBにする操作を{}内に記入
        # この辺、DBに対する具体的な操作が多数書かれているのを確認する。
        # Userオブジェクトのインスタンスを保存していることを把握するのは難しい

# リスト5.2
class UserService:
    """
    第4章で登場したUserServiceの実装

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
        # ユーザ重複が何をもって判断されるか読み取るのが難しい
        pass
