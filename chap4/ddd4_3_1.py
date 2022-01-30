"""
4.3節のコードの説明
"""
import dataclasses
from typing import Final

from chap2.ddd2_5_3 import UserId, UserName

# リスト4.7
@dataclasses.dataclass
class User:
    """
    リスト4.6で利用されているUserクラスの定義

    Attributes:
        _id (UserId): ユーザid
        name (UserName): ユーザ名

    Note:
        getterとsetterが残り、ユーザにどのようなふるまいやルールがあるかわからない
    """
    _id: Final[UserId]
    name: UserName

    @property
    def name(self) -> UserName:
        return self.name

    @name.setter
    def name(self, value: UserName):
        self.name = value

# リスト4.6
class UserService:
    """
    ドメインサービスにユーザ名変更のふるまいを記述する

    Attributes: None
    """
    def change_name(user: User, name: UserName):
        """
        ユーザ名変更

        Args:
            user (User): 変更したいユーザ
            name (UserName): 新しいユーザ名
        
        Returns: None

        Note:
            3章ではこのふるまいをエンティティに持たせた
            Userクラスはsetterを持つとする
        """
        user.name = name