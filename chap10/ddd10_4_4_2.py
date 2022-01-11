"""
10.4.4節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Any, Dict, Final

from chap4.ddd4_4_1 import UserId, UserName
from chap9.ddd9_2_0_3 import IUserFactory
from chap9.ddd9_2_2 import IUserRepository
from chap10.ddd10_3_2 import UserService
from chap10.ddd10_4_4_1 import User


# リスト10.13
class UnitOfWork(IUnitOfWork):
    """
    リポジトリに変更の追跡を移譲したユニットオブワーク
    """
    def __init__(self, connection: SqlConnection, transaction: SqlTransaction):
        self._connection: Final[SqlConnection] = connection
        self._transaction: Final[SqlTransaction] = transaction
        self.user_repository: UserRepository = UserRepository(self._connection, self._transaction)

    def commit(self):
        self._transaction.commit()
    
# リスト10.14
@dataclasses.dataclass
class UserRepository(IUserRepository):
    """
    再構築したインスタンスかどうかによって処理が分かれる
    """
    _cloned: Dict[UserId, User] = dataclasses.field(default_factory==dict, init=False)

    def find(self, id: UserId) -> User:
        # ユーザを取得するコード
        # (略)
        user = User()
        # 取得したユーザを保存
        clone_instance = self._clone(user)
        self._cloned[id] = clone_instance
        return user

    def _clone(self, user: User) -> User:
        return User(user.id, user.name)

    def save(self, user: User):
        if user.id in self._cloned:
            self._save_update(self._cloned[user.id], user)
        else:
            self._save_new(user)

    def _save_new(user: User):
        # UPSERT処理を行う
        pass

    def _save_update(self, recent: User, latest: User):
        # 変化した項目に応じてUPDATE文を組み立てて実行
        pass

# リスト10.15
@dataclasses.dataclass
class UserApplicationService:
    """
    リスト10.14を利用したユーザ登録処理
    """
    _uow: Final[IUnitOfWork]
    _user_service: Final[UserService]
    _user_factory: Final[IUserFactory]

    def register(self, command: UserRegisterCommand):
        user_name = UserName(command.name)
        user = self._user_factory.create(user_name)

        if self._user_service.exists(user):
            raise CanNotRegisterUserException(user)

        # ユニットオブワークが保持するリポジトリに永続化を依頼
        self._uow.user_repository.save(user)
        self._uow.commit()

# リスト10.16
class InMemoryUnitOfWork(IUnitOfWork):
    """
    テスト用のユニットオブワーク
    """
    def __init__(self) -> None:
        self.user_repository: InMemoryUserRepository = InMemoryUserRepository()

    def commit(self):
        if self.user_repository is not None:
            self.user_repository.commit()

# リスト10.17
@dataclasses.dataclass
class InMemoryUserRepository(IUserRepository):
    """
    インメモリのリポジトリでコミットなどが行えるようにする
    """
    _creates: Dict[str, User] = dataclasses.field(default_factory==dict, init=False)
    _updates: Dict[str, User] = dataclasses.field(default_factory==dict, init=False)
    _deletes: Dict[str, User] = dataclasses.field(default_factory==dict, init=False)
    _db: Dict[str, User] = dataclasses.field(default_factory==dict, init=False)

    def data(self) -> Dict[str, User]:
        return dict(self._db.items()-self._deletes.items()).update(self._creates).update(self._updates)

    def save(self, user: User):
        raw_user_id = user.id.value
        target_map = self._updates if raw_user_id in self.data() else self._creates
        target_map[raw_user_id] = self._clone(user)

    def remove(self, user: User):
        self._deletes[user.name.value] = self._clone(user)

    def commit(self):
        self._db = self.data()
        self._creates.clear()
        self._updates.clear()
        self._deletes.clear()

# リスト10.18
class InMemoryRepository(metaclass=ABCMeta):
    """
    リスト10.17のコードを共通化する
    """
    # 本当はAnyではなくkeyとvalueはそれぞれ共通の型と言うことにしたかったが、やり方わからなかった
    _creates: Dict[Any, Any] = dataclasses.field(default_factory==dict, init=False)
    _updates: Dict[Any, Any] = dataclasses.field(default_factory==dict, init=False)
    _deletes: Dict[Any, Any] = dataclasses.field(default_factory==dict, init=False)
    _db: Dict[Any, Any] = dataclasses.field(default_factory==dict, init=False)

    def data(self) -> Dict[Any, Any]:
        return dict(self._db.items()-self._deletes.items()).update(self._creates).update(self._updates)

    def save(self, entity: Any):
        id = self._get_id(entity)
        target_map = self._updates if id in self.data() else self._creates
        target_map[id] = self._clone(entity)

    def remove(self, entity: Any):
        id = self._get_id(entity)
        self._deletes[id] = self._clone(entity)

    def commit(self):
        self._db = self.data()
        self._creates.clear()
        self._updates.clear()
        self._deletes.clear()

    @abstractmethod
    def _get_id(self, entity: Any) -> Any:
        pass

    @abstractmethod
    def _clone(self, entity: Any) -> Any:
        pass