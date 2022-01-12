"""
11.3節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Final, List

from chap2.ddd2_5_3 import User

# リスト11.1
@dataclasses.dataclass(frozen=True)
class CircleId:
    """
    サークルの識別子となる値オブジェクト
    """
    _value: Final[str]

# リスト11.2
class CircleName:
    """
    サークルの名前を表す値オブジェクト
    """
    def __init__(self, value: str) -> None:
        if value is None: raise TypeError("NoneType")
        if len(value) < 3: raise ValueError("サークル名は3文字以上です。")
        if len(value) > 20: raise ValueError("サークル名は20文字以下です。")
        self.value: Final[str] = value

    def __eq__(self, obj: object) -> bool:
        if obj is None: return False
        if type(obj) != type(self): return False
        return self.value == obj.value

    def __hash__(self) -> int:
        return 0 if self.value is None else hash(self.value)

# リスト11.3
# リスト11.11
@dataclasses.dataclass
class Circle:
    """
    サークルを表すエンティティ
    """
    id: Final[CircleId]
    _name: CircleName
    _owner: User
    _members: List[User]

    def name(self):
        return self._name

    def owner(self):
        return self._owner

    def members(self):
        return self._members

# リスト11.4
class ICircleRepository(metaclass=ABCMeta):
    """
    サークルのレポジトリ
    """
    @abstractmethod
    def save(self, circle: Circle):
        pass

    @abstractmethod
    def find_by_id(self, id: CircleId) -> Circle:
        pass

    @abstractmethod
    def find_by_name(self, name: CircleName) -> Circle:
        pass

# リスト11.5
class ICircleFactory(metaclass=ABCMeta):
    """
    サークルのファクトリ
    """
    @abstractmethod
    def create(self, name: CircleName, owner: User) -> Circle:
        pass

# リスト11.6
@dataclasses.dataclass
class CircleService:
    """
    サークルの重複確認を行うドメインサービス
    """
    _circle_repository: Final[ICircleRepository]

    def exists(self, circle: Circle) -> bool:
        duplicated = self._circle_repository.find(circle.name)
        return duplicated is not None
