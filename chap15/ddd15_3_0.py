"""
15.3節のコードの説明
"""

# リスト15.1
class UserApplicationService:
    """
    ユーザを登録する処理はいずこに
    """
    def save_new(self, command: UserSaveNewCommand):
        pass

    def update(self, command: UserUpdateCommand):
        pass

    def remove(self, command: UserRemoveCommand):
        pass