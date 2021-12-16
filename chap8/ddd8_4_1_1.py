"""
8.4.1節のコードの説明
"""
import unittest

from chap5.ddd5_2_1 import UserService
from chap5.ddd5_6 import InMemoryUserRepository
from chap6.ddd6_2_1 import UserName
from chap6.ddd6_3_3 import UserApplicationService

# リスト8.13
class TestUserRegisterMethods(unittest.TestCase):

    def test_success_min_user_name(self):
        user_repository = InMemoryUserRepository()
        user_service = UserService(user_repository)
        user_application_service = UserApplicationService(user_repository, user_service)

        user_name = "123"
        min_user_name_input_data = UserRegisterCommand(user_name)
        user_application_service.register(min_user_name_input_data)

        created_user_name = UserName(user_name)
        created_user = user_repository.find(created_user_name)
        self.assertIsNotNone(created_user)

    def test_success_max_user_name(self):
        user_repository = InMemoryUserRepository()
        user_service = UserService(user_repository)
        user_application_service = UserApplicationService(user_repository, user_service)

        user_name = "12345678901234567890"
        max_user_name_input_data = UserRegisterCommand(user_name)
        user_application_service.register(max_user_name_input_data)

        created_user_name = UserName(user_name)
        max_user_name_user = user_repository.find(created_user_name)
        self.assertIsNotNone(max_user_name_user)