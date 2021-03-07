"""
5.6節のコードの説明
"""
from typing import Dict, Optional
import unittest
from ddd5_3_1 import IUserRepository

# リスト5.13
class InMemoryUserRepository(IUserRepository):
    """
    連想配列をベースとしたレポジトリ

    Attributes:
        store (Dict[UserId, User]): テストデータ
    """
    def __init__(self):
        self.store: Dict[UserId, User] = dict()

    def find(user_name: UserName) -> Optional[User]:
        """
        ユーザ名からユーザを探す

        Args:
            user_name (UserName): 探したいユーザ名
        
        Returns:
            Optional[User]: そのユーザ名のユーザがいる場合はUserインスタンス
                            いない場合はNone
        """
        target: Optional[User] = next(filter(
            lambda user: user.name == user_name, self.store.values()
            ), None)

        if target is not None:
            return self.clone(target)
        else:
            None
    
    def save(user: User):
        """
        保存する

        Args:
            user (User): 保存するUserインスタンス
        
        Returns: None
        """
        self.store[user.id] = self.clone(user)
    
    def clone(user: User):
        """
        ディープコピーを行う

        Args:
            user (User): ディープコピーするUserインスタンス
        
         Returns:
            User: ディープコピーしたUserインスタンス
        """
        return User(user.id, user.name)

# リスト5.14
# InMemoryUserRepositoryの中に入れる
def find(name: UserName) -> Optional[User]:
        """
        ユーザ名からユーザを探す

        Args:
            user_name (UserName): 探したいユーザ名
        
        Returns:
            Optional[User]: そのユーザ名のユーザがいる場合はUserインスタンス
                            いない場合はNone

        Note:
            リスト5.13のfindを繰り返し構文で記述したとき
        """
        for elem in self.store.values():
            if elem.name == name: return self.clone(elem)
        return None

# リスト5.15
def list5_15():
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
def list5_16():
    """
    保存処理後にリポジトリ内部のインスタンスに影響してしまう

    Args: None

    Returns: None
    """
    # ここでインスタンスをそのままリポジトリに保存してしまうと
    user_repository.save(user))
    # インスタンスの操作がリポジトリ内部に保存したインスタンスにまで影響する
    user.change_user_name(UserName("naruse"))

# リスト5.17
class TestUserRepository(unittest.TestCase):
    """
    ユーザ作成処理をテストする
    """
    def test_create_user(self):
        user_repository : InMemoryUserRepository = InMemoryUserRepository()
        program: program = Program(user_repository)
        program.create_user("nrs")

        # データを取り出して確認
        head: User = next(user_repository.store.values(), None)
        self.assertEqual(head.name, "nrs")