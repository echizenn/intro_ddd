"""
14.2.3節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Final

from chap6.ddd6_2_1 import UserId, IUserRepository
from chap6.ddd6_2_3_2 import UserData

# リスト14.6
class IUserGetInputPort(metaclass=ABCMeta):
    """
    InputPortの実装
    """
    @abstractmethod
    def handle(self, input_data: UserGetInputData):
        pass

# リスト14.7
@dataclasses.dataclass(frozen=True)
class UserGetInteractor(IUserGetInputPort):
    """
    Interactorの実装
    """
    _user_repository: Final[IUserRepository]
    _presenter: Final[IUserGetPresenter]

    def handle(self, input_data: UserGetInputData):
        target_id = UserId(input_data.user_id)
        user = self._user_repository.find_by_id(target_id)

        user_data = UserData(user.id.value, user.name.value)
        output_data = UserUpdateOutputData(user_data)
        self._presenter.output(output_data)

# リスト14.8
@dataclasses.dataclass
class StubGetInteractor(IUserGetInputPort):
    """
    テスト用のスタブ
    """
    _presenter: Final[IUserGetPresenter]

    def handle(self, input_data: UserGetInputData):
        user_data = UserData("test-id", "test-user-name")
        output_data = UserUpdateOutputdata(user_data)
        self._presenter.output(output_data)