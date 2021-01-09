"""
3.2.3節のコードの説明
"""
from typing import Final

from ddd3_2_2 import UserId

# リスト3.5
class User:
    """
    同一性の判断をするために識別子を追加

    Attributes:
        _id (UserId): ユーザ識別子
        _name (str): ユーザ名
    """
    def __init__(self, id: UserId, name: str):
        self._id: Final[UserId] = id
        self.change_user_name(name)
    
    def change_user_name(self, name: str):
        """
        外部からユーザ名を変えられるようにする

        Args:
            name (str): 新しいユーザ名
        
        Returns: None

        Raises:
            ValueError: 新しいユーザ名が3文字未満のとき
        
        Note:
            ユーザ名は3文字以上です
            振る舞いでユーザ名が変更できるようになっている。
        """
        if len(name) < 3: raise ValueError("ユーザ名は3文字以上です。")
        self._name: str = name