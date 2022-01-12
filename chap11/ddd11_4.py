"""
11.4節のコードの説明
"""
from typing import Final
import dataclasses

from chap11.ddd11_3 import CircleId, CircleName, CircleService, ICircleFactory, ICircleRepository
from chap2.ddd2_5_3 import UserId


# リスト11.7
@dataclasses.dataclass
class CircleCreateCommand:
    """
    サークル作成処理のコマンドオブジェクト
    """
    _user_id: Final[str]
    _name: Final[str]

    def user_id(self) -> str:
        return self._user_id
    
    def name(self) -> str:
        return self._name

# リスト11.8
@dataclasses.dataclass
class CircleApplicationService:
    """
    アプリケーションサービスにサークル作成処理を追加する
    """
    _circle_factory: Final[ICircleFactory]
    _circle_repository: Final[ICircleRepository]
    _circle_service: Final[CircleService]
    _user_repository: Final[IUserRepository]

    def create(self, command: CircleCreateCommand):
        with TransactionScope as transaction:
            onwer_id = UserId(command.user_id())
            owner = self._user_repository.find(onwer_id)
            if owner is None: raise UserNotFoundException("サークルのオーナーとなるユーザが見つかりませんでした。")

            name = CircleName(command.name())
            circle = self._circle_factory.create(name, owner)
            if self._circle_service.exists(circle): raise CanNotRegisterCircleException("サークルはすでに存在しています。")

            self._circle_repository.save(circle)

            transaction.complete()

    # リスト11.10
    def join(self, command: CircleJoinCommand):
        """
        アプリケーションサービスにサークル参加処理を追加する
        """
        with TransactionScope as transaction:
            member_id = UserId(command.user_id())
            member = self._user_repository.find(member_id)
            if member is None: raise UserNotFoundException("ユーザが見つかりませんでした。")

            id = CircleId(command.circle_id())
            circle = self._circle_repository.find_by_id(id)
            if circle is None: raise CircleNotFoundException("サークルが見つかりませんでした。")

            # サークルのオーナーを含めて30名か確認
            if len(circle.members()) >= 29: raise CircleFullException(id)

            # メンバーを追加する
            circle.members().append(member)
            self._circle_repository.save(circle)

            transaction.complete()

    # リスト11.12
    def invite(self, command: CircleInviteCommand):
        """
        メンバー勧誘を行う処理
        """
        with TransactionScope as transaction:
            from_user_id = UserId(command.from_user_id())
            from_user = self._user_repository.find(from_user_id)
            if from_user is None: raise UserNotFoundException("招待元ユーザが見つかりませんでした。")

            invited_user_id = UserId(command.invited_user_id)
            invited_user = self._user_repository.find(invited_user_id)
            if invited_user is None: raise UserNotFoundException("招待先ユーザが見つかりませんでした。")

            circle_id = CircleId(command.circle_id())
            circle = self._circle_repository.find_by_id(circle_id)
            if circle is None: raise CircleNotFoundException("サークルが見つかりませんでした。")

            # サークルのオーナーを含めて30名か確認
            if len(circle.members()) >= 29: raise CircleFullException(circle_id)

            circle_invitation = CircleInvitatioon(circle, from_user, invited_user)
            self._circle_invitation_repository.save(circle_invitation)
            transaction.complete()
            

# リスト11.9
@dataclasses.dataclass
class CircleJoinCommand:
    """
    サークル参加処理のコマンドオブジェクト
    """
    _user_id: Final[str]
    _circle_id: Final[str]

    def user_id(self) -> str:
        return self._user_id
    
    def circle_id(self) -> str:
        return self._circle_id

