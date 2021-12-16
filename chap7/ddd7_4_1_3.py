"""
7.4.1節のコードの説明
"""
from injector import Injector, Module

# リスト7.12
class ServiceLocator(Module):
    def configure(self, binder):
        binder.bind(IUserRepository, to=InMemoryUserRepository)

injector = Injector([ServiceLocator()])
user_application_service =  = injector.get(UserApplicationService)


# リスト7.13
class UserApplicationService:
    """
    UserApplicationServiceに変化が起きた
    """
    @inject
    def __init__(self, user_repository: IUserRepository,
                                                foo_repository: IFooRepository):
        self._user_repository = user_repository
        self._foo_repository = foo_repository