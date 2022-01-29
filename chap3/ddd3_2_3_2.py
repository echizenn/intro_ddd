"""
3.2.3節のコードの説明
"""
from __future__ import annotations # これで自己クラスを型ヒントで使える
from typing import Final

from ddd3_2_2 import UserId

# リスト3.6
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

    def __eq__(self, other: User) -> bool:
        """
        比較手段の実装

        Args:
            other (User): 比較相手のUserオブジェクト
        
        Returns:
            bool: 同一性を持つか否か

        Note:
            Pythonでは__eq__メソッドがあれば
            __hash__メソッド(本でのGetHashCodeに当たる)は不要
            むしろ実装してはいけない

            UserIdはdataclass(eq=True)としているので比較可能
        """
        if type(self) != type(other): return False
        return self._id == other._id
    
    def change_user_name(self, name: str):
        """
        外部からユーザ名を変えられるようにする

        Args:
            name (str): 新しいユーザ名
        
        Returns: None

        Raises:
            ArgumentException: 新しいユーザ名が3文字未満のとき
        
        Note:
            ユーザ名は3文字以上です
            振る舞いでユーザ名が変更できるようになっている。
        """
        if len(name) < 3: raise ArgumentException("ユーザ名は3文字以上です。", str(name))
        self._name: str = name

# リスト3.7
def check(left_user: User, right_user: User):
    """
    エンティティの比較を行う
    
    Args:
        left_user (User): 比較したいユーザ
        right_user (User): 比較対象のユーザ
    
    Returns: None
    
    Note:
        エンティティを適切に比較できるようになる
    """
    if left_user == right_user:
        print("同一のユーザです")
    else:
        print("別のユーザです")