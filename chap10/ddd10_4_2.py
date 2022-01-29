"""
10.4.2節のコードの説明
"""
import dataclasses
from typing import Final

from chap4.ddd4_4_1 import UserName
from chap9.ddd9_2_0_3 import IUserFactory
from chap9.ddd9_2_2 import IUserRepository
from chap10.ddd10_3_2 import UserService

# リスト10.7
@dataclasses.dataclass
class UserApplicationService:
    """
    トランザクションスコープを利用する
    """
    _user_service: Final[UserService]
    _user_factory: Final[IUserFactory]
    _user_repository: Final[IUserRepository]

    def register(self, command: UserRegisterCommand):
        """
        トランザクションを利用するようにユーザ登録処理を書き換える

        Raises:
            CanNotRegisterUserException: 同一ユーザが存在している場合
        """
        # トランザクションスコープを生成する
        # with句のスコープ内でコネクションが開かれると自動的にトランザクションが開始されるとする
        with TransactionScope as transaction:
            user_name = UserName(command.name)
            user = self._user_factory.create(user_name)
            
            if self._user_service.exists(user):
                raise CanNotRegisterUserException(user, "ユーザはすでに存在しています。")
            
            self._user_repository.save(user)
            # 処理を反映する際にはコミット処理を行う
            transaction.complete() # このようなコマンドがあると仮定する