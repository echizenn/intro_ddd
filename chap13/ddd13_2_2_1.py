"""
13.2.2節のコードの説明
"""
import dataclasses
import datetime
import dateutil
from typing import Final

# リスト13.12
@dataclasses.dataclass(frozen=True)
class CircleRecommendSpecification:
    """
    お勧めサークルかどうかを見極める仕様オブジェクト
    """
    _execute_date_time: Final[datetime.date]

    def is_satisfied_by(self, circle: Circle) -> bool:
        if circle.count_members() < 10: return False
        return circle.created > self._execute_date_time - dateutil.relativedelta.relativedelta(months=1)

# リスト13.13
@dataclasses.dataclass(frozen=True)
class CircleApplicationService:
    """
    仕様を利用しお勧めサークルを検索する
    """
    _circle_repository: Final[ICircleRepository]
    _now: Final[datetime.date]

    def get_recommend(self, request: CircleGetRecommendRequest) -> CircleGetRecommendResult:
        recommend_circle_spec = CircleRecommendSpecification(self._now)

        circles = self._circle_repository.find_all()
        recommend_circles = [circle for circle in circles if recommend_circle_spec.is_satisfied_by(circle)][:10]

        return CircleGetRecommendResult(recommend_circles)
