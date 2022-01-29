"""
10.4.4節のコードの説明
"""
from abc import ABCMeta
import dataclasses
from typing import Any, Final

from chap4.ddd4_4_1 import UserName
from chap9.ddd9_2_0_3 import IUserFactory
from chap9.ddd9_2_2 import IUserRepository
from chap10.ddd10_3_2 import UserService

# リスト10.9
class UnitOfWork:
    """
    ユニットオブワークの定義
    """

    def register_now(self, value: Any):
        pass

    def register_dirty(self, value: Any):
        pass

    def register_clean(self, value: Any):
        pass

    def register_deleted(self, value: Any):
        pass

    def commit(self, value: Any):
        pass

# リスト10.10
class Entity(metaclass=ABCMeta):
    def _mark_new(self):
        UnitOfWork.current.register_new(self) # このcurrentが何を表しているのかよくわからない…

    def _mark_clean(self):
        UnitOfWork.current.register_clean(self)

    def _mark_dirty(self):
        UnitOfWork.current.register_dirty(self)

    def _mark_deleted(self):
        UnitOfWork.current.register_deleted(self)

# リスト10.11
class User(Entity):
    def __init__(self, name: UserName):
        self._name: UserName = name
        self._mark_new()

    def change_name(self, name: UserName):
        self._name = name
        self._mark_dirty()
        
# リスト10.12
@dataclasses.dataclass
class UserApplicationService:
    """
    ユニットオブワークを利用したユーザ登録処理
    """
    # ユニットオブワークを保持する
    _uow: Final[UnitOfWork]
    _user_service: Final[UserService]
    _user_factory: Final[IUserFactory]
    _user_repository: Final[IUserRepository]

    def register(self, command: UserRegisterCommand):
        """
        Raises:
            CanNotRegisterUserException: 同一ユーザが存在している場合
        """
        user_name = UserName(command.name)
        user = self._user_factory.create(user_name)

        if self._user_service.exists(user):
            raise CanNotRegisterUserException("ユーザはすでに存在しています")

        self._user_repository.save(user)

        # 作業結果の反映をユニットオブワークに伝える
        self._uow.commit()
        