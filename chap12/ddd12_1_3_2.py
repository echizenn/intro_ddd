"""
12.1.3節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Final

from chap4.ddd4_4_1 import UserId, UserName
from chap9.ddd9_2_2 import IUserRepository

# リスト12.11
class IUserNotification(metaclass=ABCMeta):
    """
    通知のためのインターフェース
    """
    @abstractmethod
    def id(self, id: UserId):
        pass

    @abstractmethod
    def name(self, name: UserName):
        pass

# リスト12.12
@dataclasses.dataclass
class UserDataModelBuilder(IUserNotification):
    """
    リスト12.11を実装した通知オブジェクト
    """
    # 通知されたデータはインスタンス変数で保持される
    _id: UserId
    _name: UserName

    def id(self, id: UserId):
        self._id = id

    def name(self, name: UserName):
        self._name = name

    # 通知されたデータからデータモデルを生成するメソッド
    def build(self) -> UserDataModel:
        return UserDataModel(id=self._id.value, name=self._name.value)

# リスト12.13
@dataclasses.dataclass
class User:
    """
    通知オブジェクトを受け取るメソッドを追加する
    """
    # インスタンス変数はいずれも非公開
    _id: Final[UserId]
    _name: UserName

    def notify(self, note: IUserNotification):
        # 内部データを通知
        note.id(self._id)
        note.name(self._name)

# リスト12.14
class EFUserRepository(IUserRepository):
    """
    通知オブジェクトを利用してデータモデルを取得する
    """
    def save(self, user: User):
        # 通知オブジェクトを引き渡しダブルディスパッチにより内部データを取得
        user_data_model_builder = UserDataModelBuilder()
        user.notify(user_data_model_builder)

        # 通知された内部データからデータモデルを生成
        user_data_model = user_data_model_builder.build()

        # データモデルをO/R Mapperに引き渡す
        self._context["Users"].insert(user_data_model)
        self._context.save_changes() # これはあっているかわからない