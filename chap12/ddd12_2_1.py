"""
12.2.1節のコードの説明
"""
import dataclasses
from typing import Final, List

from chap4.ddd4_4_1 import UserId
from chap11.ddd11_3 import CircleId, CircleName, ICircleRepository


# リスト12.19
@dataclasses.dataclass
class Circle:
    """
    識別子をインスタンスの代わりとして保持する
    """
    ＿id: Final[CircleId]
    _name: CircleName
    # _members: List[User]
    _members: List[UserId]

    def id(self) -> CircleId:
        return self._id

    def name(self) -> CircleName:
        return self._name

    def members(self) -> List[UserId]:
        return self._members

# リスト12.20
@dataclasses.dataclass
class CircleApplicationService:
    _circle_repository: Final[ICircleRepository]

    def update(self, command: CircleUpdateCommand):
        with TransactionScope() as transaction:
            id = CircleId(command.id)
            # この時点でUserのインスタンスが再構築されるが
            circle = self._circle_repository.find(id)
            if circle is None: raise CircleNotFoundException(id)

            if command.name is not None:
                name = CircleName(command.name)
                circle.change_name(name)
            
                if self._circle_service.exists(circle):
                    raise CanNotRegisterCircleException(circle, "サークルは既に存在しています。")
            
            self._circle_repository.save(circle)

            transaction.complete()

            # Userのインスタンスは使われることなく捨てられる