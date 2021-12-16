"""
8.4.2節のコードの説明
"""
from typing import Dict
import unittest

from chap5.ddd5_2_1 import UserService
from chap6.ddd6_2_1 import UserName
from chap6.ddd6_3_3 import UserApplicationService

# リスト8.14
class InMemoryUserRepository:
    store: Dict[UserId, User]=dict()

# リスト8.15
class TestUserRegisterMethods(unittest.TestCase):

    def test_success_min_user_name(self):
        user_repository = InMemoryUserRepository()
        user_service = UserService(user_repository)
        user_application_service = UserApplicationService(user_repository, user_service)

        user_name = "123"
        min_user_name_input_data = UserRegisterCommand(user_name)
        user_application_service.register(min_user_name_input_data)

        created_user = next(filter(lambda user: user.name==user_name, user_repository.store.values), None)
        self.assertIsNotNone(created_user)

    # リスト8.16
    def test_invalid_user_name_length_min(self):
        user_repository = InMemoryUserRepository()
        user_service = UserService(user_repository)
        user_application_service = UserApplicationService(user_repository, user_service)

        exception_occured = False
        try:
            command = UserRegisterCommand("12")
            user_application_service.register(command)
        except:
            exception_occured = True
        
        self.assertTrue(exception_occured)

    def test_invalid_user_name_length_max(self):
        user_repository = InMemoryUserRepository()
        user_service = UserService(user_repository)
        user_application_service = UserApplicationService(user_repository, user_service)

        exception_occured = False
        try:
            command = UserRegisterCommand("123456789012345678901")
            user_application_service.register(command)
        except:
            exception_occured = True
        
        self.assertTrue(exception_occured)

    # リスト8.17
    def test_already_exists(self):
        user_repository = InMemoryUserRepository()
        user_service = UserService(user_repository)
        user_application_service = UserApplicationService(user_repository, user_service)

        user_name = "test-user"
        user_repository.save(User(UserId("test-id"), UserName(user_name)))

        exception_occured = False
        try:
            command = UserRegisterCommand(user_name)
            user_application_service.register(command)
        except:
            exception_occured = True
        
        self.assertTrue(exception_occured)