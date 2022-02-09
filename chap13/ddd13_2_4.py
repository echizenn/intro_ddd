"""
13.2.4節のコードの説明
"""
import dataclasses
from typing import Final, List

import sqlalchemy


# リスト13.18
class CircleApplicationService:
    """
    サークル一覧を取得する処理

    Note:
        とにかく遅い
    """
    def get_summaries(self, command: CircleGetSummariesCommand) -> CircleGetSummariesResult:
        # 全件取得して
        all = self._circle_repository.findall()
        # その後にページング
        circles = all[(command.page-1) * command.size: (command.page-1) * command.size+command.size]

        summaries: List[CircleSummaryData] = list()
        for circle in circles:
            # サークルのオーナーを改めて検索
            owner = self._user_repository.find(circle.owner)
            summaries.append(CircleSummaryData(circle.id.value, owner.name.value))
            
        return CircleGetSummariesResult(summaries)

# リスト13.19
class CircleQueryService:
    """
    最適化のために直接クエリを実行する
    """
    def get_summaries(self, command: CircleGetSummariesCommand) -> CircleGetSummariesResult:
        connection = self.provider.connection

        with connection.create_command() as sql_command:
            sql_command.command_text = """SELECT
            circles.id as circleId, users.name as onwerName
            FROM circles
            LEFT OUTER JOIN users
             ON circles.ownerId = users.id
             ORDER BY circles.id
             OFFSET ? ROWS
             FETCH NEXT ? ROWS ONLY
            """
            page = command.page
            size = command.size
            sql_command.parameters.add(SqlParameter("@skip", (page-1)*size))
            sql_command.parameters.add(SqlParameter("@size", size))

            with sql_command.execute_reader() as reader:
                summaries: List[CircleSummaryData] = list()
                while reader.read():
                    circle_id = str(reader["circleId"])
                    owner_name = str(reader["ownerName"])
                    summary = CircleSummaryData(circle_id, owner_name)
                    summaries.append(summary)
                
                return CircleGetSummariesResult(summaries)

# リスト13.20
@dataclasses.dataclass
class DatasetCircleQueryService:
    """
    これまでORMにdatasetを用いてきたが、datasetではJOIN句が扱えないので、
    SQLAlchemyを用いる。

    おそらく正確な書き方はできていない
    """
    _context: Final[sqlalchemy.engine.Engine]

    def get_summaries(self, command: CircleGetSummaries) -> CircleGetSummaryResult:
        SessionClass = sqlalchemy.orm.sessionmaker(self._context)
        session = SessionClass()

        all_ = session.query(Circle, User).join(User, User.id==Circle.owner_id)

        page = command.page
        size = command.size

        summaries = all_.limit(size).offset((page-1)*size).all()

        return CircleGetSummariesResult(summaries)