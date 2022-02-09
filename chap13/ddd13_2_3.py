"""
13.2.3節のコードの説明
"""
from typing import Final, List
import dataclasses

from chap13.ddd13_2_2_2 import ICircleRepository, ISpecification


# リスト13.17
@dataclasses.dataclass
class CircleRepository(ICircleRepository):
    """
    仕様オブジェクトを受け取るリポジトリの実装

    Note:
        毎回インスタンスを作成することで実行速度がかなり遅くなっている
    """
    _connection: Final[SqlConnection]

    def find(self, specification: ISpecification) -> List[Circle]:
        with self._connection.create_command() as command:
            # 全件取得するクエリを発行
            command.command_text = "SELECT * FROM circles"
            with command.execute_reader() as reader:
                circles: List[Circle] = list()
                while reader.read():
                    # インスタンスを生成して条件に合うか確認している（合わなければ捨てられる）
                    circle = self.create_instance(reader)
                    if specification.is_satisfied_by(circle):
                        circles.append(circle)
                    
                return circles