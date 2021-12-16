"""
7.4.1節のコードの説明
"""
from typing import Final

from injector import inject, Module

from ddd7_2_1 import IUserRepository

# リスト7.7
class UserApplicationService:
    @inject
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

# リスト7.8
# injectorを用いることにした
# https://github.com/alecthomas/injector
# テストしてないので動くか確認してないです
class ServiceLocator(Module):
    def configure(self, binder):
        binder.bind(IUserRepository, to=InMemoryUserRepository)