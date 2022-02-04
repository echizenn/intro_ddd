"""
5.6節のコードの説明
"""
import dataclasses
from typing import Dict, Optional
import unittest

from chap4.ddd4_4_1 import User, UserId, UserName
from ddd5_2_2 import Program
from ddd5_3_1 import IUserRepository

# リスト5.13
@dataclasses.dataclass
class InMemoryUserRepository(IUserRepository):
    """
    連想配列をベースとしたレポジトリ

    Attributes:
        store (Dict[UserId, User]): テストデータ
    """
    # テストケースによってはデータを確認したいことがある
    # 確認のための操作を外部から行えるようにするためpublicにしている
    store: Dict[UserId, User] = dict()

    def find(self, user_name: UserName) -> Optional[User]:
        """
        ユーザ名からユーザを探す

        Args:
            user_name (UserName): 探したいユーザ名
        
        Returns:
            Optional[User]: ユーザ名のユーザがいる場合はUserインスタンス
                            いない場合はNone
        """
        target: Optional[User] = next(filter(
            lambda user: user.name == user_name, self.store.values()
            ), None)

        if target is not None:
            return self.clone(target)
        else:
            None
    
    def save(self, user: User):
        """
        保存する

        Args:
            user (User): 保存するUserインスタンス
        
        Returns: None
        """
        self.store[user.id] = self.clone(user)
    
    def clone(self, user: User):
        """
        ディープコピーを行う

        Args:
            user (User): ディープコピーするUserインスタンス
        
         Returns:
            User: ディープコピーしたUserインスタンス
        """
        return User(user.id, user.name)

    # リスト5.14
    def find(self, name: UserName) -> Optional[User]:
            """
            ユーザ名からユーザを探す

            Args:
                user_name (UserName): 探したいユーザ名
            
            Returns:
                Optional[User]: ユーザ名のユーザがいる場合はUserインスタンス
                                いない場合はNone

            Note:
                リスト5.13のfindを繰り返し構文で記述したとき
            """
            for elem in self.store.values():
                if elem.name == name: return self.clone(elem)
            return None

# リスト5.15
def list5_15(user_repository: (IUserRepository)):
    """
    オブジェクトへの操作がリポジトリ内部のインスタンスに影響してしまう

    Args: None

    Returns: None
    """
    # オブジェクトを再構築する際にディープコピーを行わないと
    user: User = user_repository.find(UserName("Naruse"))
    # 次の操作がリポジトリ内部で保管されているインスタンスにまで影響する
    user.change_user_name(UserName("naruse"))

# リスト5.16
def list5_16(user_repository: IUserRepository, user: User):
    """
    保存処理後にリポジトリ内部のインスタンスに影響してしまう

    Args: None

    Returns: None
    """
    # ここでインスタンスをそのままリポジトリに保存してしまうと
    user_repository.save(user)
    # インスタンスの操作がリポジトリ内部に保存したインスタンスにまで影響する
    user.change_user_name(UserName("naruse"))

# リスト5.17
class TestUserRepository(unittest.TestCase):
    """
    ユーザ作成処理をテストする
    """
    def test_create_user(self):
        user_repository : InMemoryUserRepository = InMemoryUserRepository()
        program: Program = Program(user_repository)
        program.create_user("nrs")

        # データを取り出して確認
        head: User = next(user_repository.store.values(), None)
        self.assertEqual(head.name, "nrs")