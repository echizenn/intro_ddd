"""
7.2節のコードの説明
"""
from dataclasses import dataclass

from ddd7_2_1 import IUserRepository

# リスト7.4
@dataclass
class UserApplicationService:
    """
    ユーザーのアプリケーションサービス
    """
    _user_repository: IUserRepository