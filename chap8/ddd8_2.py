"""
8.2節のコードの説明
"""
from chap5.ddd5_2_1 import UserService
from chap5.ddd5_6 import InMemoryUserRepository
from chap7.ddd7_2_1 import IUserRepository
from chap7.ddd7_4_1_3 import UserApplicationService
from injector import Injector, Module, singleton
from typing import List

# リスト8.1
class ServiceLocator(Module):
    def configure(self, binder):
        binder.bind(IUserRepository, to=InMemoryUserRepository, scope=singleton)
        binder.bind(UserService)
        binder.bind(UserApplicationService)

class Program:
    def __init__(self, service_provider: ServiceProvider):
        self.service_provider = service_provider

    def main(self, args: List[str]):
        self.startup()
        pass

    def startup(self):
        service_collection = Injector([ServiceLocator()])
        self.service_provider = service_collection.get(ServiceProvider)