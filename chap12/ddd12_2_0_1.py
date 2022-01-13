"""
12.2節のコードの説明
"""
import dataclasses
from typing import List

from chap4.ddd4_4_1 import UserId, UserName, User
from chap11.ddd11_3 import ICircleRepository

# リスト12.16
@dataclasses.dataclass
class Circle:
    """
    サークル集約を通じてユーザ集約のふるまいを呼び出す
    """
    _members: List[User]

    def change_member_name(self, id: UserId, name: UserName):
        target = next((x for x in self._members if x.id == id), None)
        if target is not None:
            target.change_name(name)

# リスト12.17
class CircleRepository(ICircleRepository):
    """
    サークル集約を永続化する処理
    """
    def save(self, circle: Circle):
        with self._connection.create_command() as command:
            command.command_text = """MERGE INTO circles
                USING( SELECT ? AS id, ? AS name, ? AS ownerId ) AS data
                ON circles.id = data.id
                WHEN MATCHED THEN
                    UPDATE SET name = data.name, ownerId = data.ownerId
                WHEN NOT MATCHED THEN
                    INSERT (id, name, ownerId)
                    VALUES (data.id, data.name, data.ownerId)"""

            command.parameters.add(SqlParameter("@id", circle.id.value)
            command.parameters.add(SqlParameter("@name", circle.name.value)
            command.parameters.add(SqlParameter("@ownerId", circle.owner.id.value if circle.owner is not None else None)
            command.execute_non_query()

        with self._connection.create_command() as command:
            command.command_text: str = """MERGE INTO userCircles
                USING( SELECT ? AS userId, ? AS circleId ) AS data
                ON userCircles.id = data.userId AND userCircles.circleId = data.circleId
                WHEN NOT MATCHED THEN
                    INSERT (userId, circleId)
                    VALUES (data.userId, data.circleId)"""

            # 第二パラメータ以降の変数が、?の部分に代入される
            command.parameters.add(SqlParameter("@circleId", circle.id.value)
            command.parameters.add(SqlParameter("@userId", None)

            for member in circle.members:
                command.parameters["@userId"].value = member.id.value
                command.execute_non_query()