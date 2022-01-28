"""
7.2節のコードの説明
"""
import dataclasses

from ddd7_2_1 import IUserRepository

# リスト7.4
@dataclasses.dataclass
class UserApplicationService:
    """
    ユーザーのアプリケーションサービス
    """
    _user_repository: IUserRepository