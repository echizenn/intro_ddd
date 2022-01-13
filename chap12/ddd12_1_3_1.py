"""
12.1.3節のコードの説明
"""
from chap4.ddd4_4_1 import User
from chap9.ddd9_2_2 import IUserRepository

# リスト12.10
class EFUserRepository(IUserRepository):
    """
    リポジトリの永続化処理
    """
    def save(self, user: User):
        # ゲッターを利用してデータの詰め替えをしている
        user_data_model = UserDataModel(id=user.id.value, name=user.name.value)
        self._context["Users"].insert(user_data_model)
        self._context.save_changes() # これはあっているかわからない
