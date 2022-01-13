"""
12.2節のコードの説明
"""

from chap11.ddd11_3 import ICircleRepository
from chap12.ddd12_2_0_1 import Circle

# リスト12.18
class CircleRepository(ICircleRepository):
    """
    サークル集約を永続化する処理
    """
    def save(self, circle: Circle):
        # ユーザ集約に対する更新処理を行う
        with self._connection.create_command() as command:
            command.command_text = """UPDATE users SET username = ? WHERE id = @id"""
            command.parameters.add(SqlParameter("@id", None)
            command.parameters.add(SqlParameter("@username", None)

            for user in circle.members:
                command.parameters["@id"].value = user.id.value
                command.parameters["@username"].value = user.name.value
                command.execute_non_query()

        # その後サークルの更新処理を行う
        pass