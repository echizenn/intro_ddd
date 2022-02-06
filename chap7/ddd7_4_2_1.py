"""
7.4節のコードの説明

PythonではService Locatorパターンの実装がわからなかったことと、
ServiceLocatorパターンよりはIoC Containerパターンの方が依存関係がわかりやすいという
説明から、Service Locatorパターンは実装しないことにする。
"""
import dataclasses
from typing import Final

from ddd7_2_1 import IUserRepository

# リスト7.14
def list7_14():
    """
    依存を注入する

    Note:
        コンストラクタで依存するオブジェクトを注入している(これまで)
    """
    user_repository = InMemoryUserRepository()
    user_application_service = UserApplicationService(user_repository)

# リスト7.15
@dataclasses.dataclass(frozen=True)
class UserApplicationService:
    """
    新たな依存関係を追加する
    """
    _user_repository: Final[IUserRepository]
    # 新たにIFooRepositoryへの依存関係を追加する
    _foo_repository: Final[IFooRepository]

# リスト7.16
def list7_16():
    """
    テストがエラーになる
    """
    user_repository = InMemoryUserRepository()
    # 第２引数にIFooRepositoryの実態が渡されていないためコンパイルエラーとなる
    user_application_service = UserApplicationService(user_repository)