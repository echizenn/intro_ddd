"""
7.4節のコードの説明

PythonではService Locatorパターンの実装がわからなかったことと、
ServiceLocatorパターンよりはIoC Containerパターンの方が依存関係がわかりやすいという
説明から、Service Locatorパターンは実装しないことにする。

PythonのDIツールとして、injectorを用いることにした。
https://github.com/alecthomas/injector
"""
import dataclasses
from typing import Any, Final

import injector

from ddd7_2_1 import IUserRepository

# リスト7.17
@injector.inject
@dataclasses.dataclass(frozen=True)
class UserApplicationService:
    _user_repository: Final[IUserRepository]


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
