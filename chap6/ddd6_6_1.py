"""
6.6節のコードの説明
"""
from dataclasses import dataclass

# リスト6.39
# ddd6_4.pyなど参照

# リスト6.40
@dataclass
class UserApplicationService:
    """
    自身のふるまいを変化させる目的で状態を持つサービスの例
    """
    _send_mail: bool

    def register(self):
        """
        ユーザー登録

        Args: 省略

        Returns: 省略
        """
        # 色々な処理をする

        # 自身の状態によってふるまいが変化する
        if self._send_mail:
            MailUtility.send("user registered")