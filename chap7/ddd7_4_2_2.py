"""
7.4節のコードの説明

PythonではService Locatorパターンの実装がわからなかったことと、
ServiceLocatorパターンよりはIoC Containerパターンの方が依存関係がわかりやすいという
説明から、Service Locatorパターンは実装しないことにする。

PythonのDIツールとして、injectorを用いることにした。
https://github.com/alecthomas/injector
"""
import injector
from typing import Any

from ddd7_2_1 import IUserRepository

# リスト7.17
class UserApplicationService:
    @injector.inject
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository


class ServiceCollection:
    def __init__(self) -> None:
        self.injector = injector.Injector(self.__class__.configure)

    @classmethod
    def configure(binder):
        """
        依存関係の登録をする
        """
        binder.bind(IUserRepository, to=InMemoryUserRepository)

    def resolve(self, cls: Any) -> Any:
        return self.injector.get(cls)


def list7_17():
    """
    IoC Containerを利用して依存関係を解決させる
    """
    service_collection = ServiceCollection()

    # インスタンスはIoC Container経由で取得する
    user_application_service = service_collection.resolve(UserApplicationService)
