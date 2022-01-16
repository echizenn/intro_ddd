"""
14.2.1節のコードの説明
"""
import dataclasses
from typing import Final, List, Union

# flaskでそれっぽく書く
# 以下のコードで動くか保証はできません
import flask

app = flask.Flask(__name__)

# リスト14.1
@dataclasses.dataclass
class UserController(flask.views.MethodView):
    """
    プレゼンテーション層の住人であるコントローラ
    """
    _user_application_service = Final[UserApplicationService]

    def index(self):
        result  = self._user_application_service.get_all()
        users = [UserResponseModel(x.id, x.name) for x in result.users]

        return UserIndexResponseModel(users)

    def get(self):
        if flask.request.args.get("id") is None:
            return self.index()
        id = flask.request.args.get("id")
        command = UserGetCommand(id)
        result = self._user_application_service.get(command)

        user_model = UserResponseModel(result.user)

        return UserGetResponseModel(user_model)

    def post(self):
        command = UserRegisterCommand(flask.request.form["Username"])
        result = self._user_application_service.register(command)
        return UserPostResponseModel(result.created_user_id)

    def put(self):
        id = flask.request.args.get("id")
        command = UserUpdateCommand(id, flack.request.form["Name"])
        self._user_application_service.update(command)

    def delete(self):
        id = flask.request.args.get("id")
        command = UserDeleteCommand(id)
        self._user_application_service.delete(command)

# リスト14.2
@dataclasses.dataclass
class UserApplicationService:
    """
    アプリケーション層の住人であるアプリケーションサービス
    """
    _user_factory: Final[IUserFactory]
    _user_repository: Final[IUserRepository]
    _user_service: Final[UserService]

    def get(self, command: UserGetCommand) -> UserGetResult:
        id = UserId(command.id)
        user = self._user_repository.find(id)
        if user is None: return UserNotFoundException(id, "ユーザが見つかりませんでした。")

        data = UserData(user)

        return UserGetResult(data)

    def get_all(self) -> UserGetAllResult:
        users = self._user_repository.find_all()
        user_models = [UserData(x) for x in users]
        return UserGetAllResult(user_models)
    
    def register(self, command: UserRegisterCommand) -> UserRegisterResult:
        with TransactionScope() as transaction:
            name = UserName(command.name)
            user = self._user_factory.create(name)
            if self._user_service.exists(user): return CanNotRegisterUserException(user, "ユーザは既に存在しています。")

            self._user_repository.save(user)

            transaction.complete()

            return UserRegisterResult(user.id.value)

    def update(self, command: UserUpdateCommand) -> UserUpdateResult:
        with TransactionScope() as transaction:
            id = UserId(command.id)
            user = self._user_repository.find(id)
            if user is None: return UserNotFoundException(id)

            if command.name is not None:
                name = UserName(command.name)
                user.change_name(name)

                if self._user_service.exists(user): return CanNotRegisterUserException(user, "ユーザは既に存在しています。")
            
            self._user_repository.save(user)

            transaction.complete()

    def delete(self, command: UserDeleteCommand):
        with TransactionScope() as transaction:
            id = UserId(command.id)
            user = self._user_repository.find(id)
            if user is None: return

            self._user_repository.delete(user)

            transaction.complete()

# リスト14.3
class User:
    """
    ドメイン層の住人であるエンティティ
    """
    def __init__(self, id: UserId, name: UserName, type: UserType):
        if id is None: return ArgumentNullException(id)
        if name is None: return ArgumentNullException(name)
        self._id: Final[UserId] = id
        self._name: UserName = name
        self._type: UserType = type

    def id(self) -> UserId:
        return self._id

    def name(self) -> UserName:
        return self._name

    def type(self) -> UserType:
        return self._type

    def is_premium(self) -> bool: return self._type == UserType.premium

    def change_name(self, name: UserName):
        if name is None: return ArgumentNullException(name)
        self._name = name

    def upgrade(self):
        self._type = UserType.Premium

    def downgrade(self):
        self._type = UserType.Normal

    def to_string(self) -> str:
        sb = ObjectValueStringBuilder(str(self._id), self._id).append(str(self._name), self._name)
        return sb.to_string()


@dataclasses.dataclass
class UserService:
    """
    ドメイン層の住人であるドメインサービス
    """
    _user_repository: Final[IUserRepository]

    def exists(self, user: User) -> bool:
        duplicated_user = self._user_repository.find(user.name)
        
        return duplicated_user is not None

# リスト14.4
@dataclasses.dataclass
class DSUserRepository(IUserRepository):
    """
    インフラストラクチャ層の住人であるリポジトリ
    """
    _context: Final[ItdddDbContext]

    def find_by_id(self, ids: Union[UserId, List[UserId]]) -> Union[User, List[User]]:
        if isinstance(ids, User):
            target = self._context.users.find(id.value)
            if target is None: return None

            return ToModel(target)
        
        raw_ids = [x.value for x in ids]

        targets = [user_data for user_data in self._context.users if user_data.id in raw_ids]

        return [ToModel(x) for x in targets]

    def find_by_name(self, name: UserName) -> User:
        target = next(filter(lambda user_data: user_data.name == name.value, self._context.users), None)
        if target is None: return None

        return ToModel(target)