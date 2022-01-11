"""
10.4.3節のコードの説明
"""
import dataclasses
from typing import Final

from chap4.ddd4_4_1 import UserName
from chap9.ddd9_2_0_3 import IUserFactory
from chap9.ddd9_2_2 import IUserRepository
from chap10.ddd10_3_2 import UserService

# リスト10.8
@dataclasses.dataclass
class UserApplicationService:
    """
    Transactionalアノテーションを利用する
    """
    _user_service: Final[UserService]
    _user_factory: Final[IUserFactory]
    _user_repository: Final[IUserRepository]

    @Transactional(isolatin = Isolation.SERIALIZABLE) # このようなデコレータがあるとする
    def register(self, command: UserRegisterCommand):
        """
        トランザクションを利用するようにユーザ登録処理を書き換える
        """
        # トランザクションスコープを生成する
        # with句のスコープ内でコネクションが開かれると自動的にトランザクションが開始されるとする
        user_name = UserName(command.get_name())
        user = self._user_factory.create(user_name)
        
        if self._user_service.exists(user):
            raise ValueError("ユーザはすでに存在しています。")
        
        self._user_repository.save(user)