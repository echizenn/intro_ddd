"""
8.2.1節のコードの説明
"""
from chap5.ddd5_2_1 import UserService
from chap5.ddd5_4 import UserRepository
from chap7.ddd7_2_1 import IUserRepository
from chap7.ddd7_4_1_3 import UserApplicationService
from injector import Injector, Module, singleton
from typing import List

# リスト8.2
# リスト8.3
class ServiceLocator(Module):
    def configure(self, binder):
        # UserRepositoryに差し替え
        # binder.bind(IUserRepository, to=InMemoryUserRepository, scope=singleton)
        binder.bind(IUserRepository, to=UserRepository, scope=singleton)
        binder.bind(UserService)
        binder.bind(UserApplicationService)

class Program:
    def __init__(self, service_provider: ServiceProvider):
        self.service_provider = service_provider

    def main(self, args: List[str]):
        self.startup()
        
        while True:
            print("Input user name")
            print(">")
            _input = input()
            usr_application_service = self.service_provider.get(UserService)
            command = UserRegisterCommand(_input)
            usr_application_service.register(command)

            print("----------------------")
            print("user created:")
            print("----------------------")
            print("user name:")
            print("- " + _input)
            print("----------------------")

            print("continue? (y/n)")
            print(">")
            yes_or_no = input()
            if yes_or_no == "n": break

    def startup(self):
        service_collection = Injector([ServiceLocator()])
        self.service_provider = service_collection.get(ServiceProvider)