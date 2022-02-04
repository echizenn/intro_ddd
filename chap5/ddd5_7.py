"""
5.7節のコードの説明
"""
import dataclasses
from typing import Final, Optional, Dict
import unittest

# pythonではdatasetというORMが簡単に扱えて、
# 本とも書き方が似ていると思うのでdatasetを採用する。
# pip install dataset
import dataset

from chap4.ddd4_4_1 import User, UserId, UserName
from ddd5_2_2 import Program
from ddd5_3_1 import IUserRepository

# リスト5.18
@dataclasses.dataclass(frozen=True)
class EFUserRepository(IUserRepository):
    """
    datasetを利用したリポジトリ

    Attributes:
        _context (dateset.Database): データベース情報、Usersテーブルを持つ
                                     Userテーブルはnameとidカラムを持つ
    """
    _context: Final[dataset.Database]

    def find(self, name: UserName) -> Optional[User]:
        """
        ユーザ名からUserインスタンスを探すメソッド

        Args:
            name (UserName): 探したいユーザ名
        
        Returns:
            Optional[User]: 見つかったUserインスタンス、ない場合はNone
        """
        target: Optional[Dict] = self._context["Users"].find_one(name=name.value)
        if target is None: return None
        return self._to_model(target)

    def save(self, user: User):
        """
        Userインスタンスを保存するメソッド

        Args:
            user (User): 保存したいUserインスタンス
        
        Returns: None
        """
        found: Optional[Dict] = self._context["Users"].find(id=user.id.value)

        if found is None:
            data: Dict = self._to_data_model(user)
            self._context["Users"].insert(data)
        else:
            data: Dict = self._transfer(user, found)
            self._context["Users"].update(data, ["id"])
    
    def _to_model(self, from_: Dict) -> User:
        """
        辞書型からUserインスタンスに変換する

        Args:
            from_ (Dict): 変換したい辞書型インスタンス

        Returns:
            User: 変換結果のUserインスタンス
        """
        return User(UserId(from_.id), UserName(from_.name))

    def _transfer(self, from_: User, model: Dict) -> Dict:
        """
        modelをfrom_の情報によって更新する

        Args:
            from_ (User): 最新情報
            model (Dict): 元々の情報
        
        Returns:
            更新された辞書型の情報
        """
        model.id = from_.id.value
        model.name = from_.name.value
        return model

    def _to_data_model(self, from_: User) -> Dict:
        """
        Userインスタンスを辞書型に変換する

        Args:
            from_ (User): 変換したいUserインスタンス
        
        Returns:
            Dict: 変換結果の辞書
        """
        return {"id": from_.id.value, "name": from_.name.value}

# リスト5.19, 5.20
# datasetではdefaultではOrderedDictがエンティティになっている
# Database.row_typeを自作クラスに変更すればエンティティの自作もできる
# その場合の細かい動きがわからないのでここでは省略する

# リスト5.21
class TestUserRepository(unittest.TestCase):
    """
    ユーザ作成処理をテストする

    Note:
        リスト5.17とリポジトリの実体が変わっているだけ
    """
    def test_create_user(self, my_context: dataset.Database):
        user_repository : EFUserRepository = EFUserRepository(my_context)
        program: Program = Program(user_repository)
        program.create_user("naruse")

        # データを取り出して確認
        head: User = my_context["Users"].find(_limit=1)
        self.assertEqual(head.name, "naruse")