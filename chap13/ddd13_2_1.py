"""
13.2.1節のコードの説明
"""
from abc import ABCMeta
import dataclasses
import datetime
from typing import Final, List

# リスト13.10
class ICircleRepository(metaclass=ABCMeta):
    """
    リポジトリにお勧めサークルを探し出すメソッドを追加する
    """
    def find_recommended(self, now: datetime.date) -> List[Circle]:
        pass

# リスト13.11
@dataclasses.dataclass(frozen=True)
class CircleApplicationService:
    """
    お勧めサークルを探し出すアプリケーションサービスの処理
    """
    _now: Final[datetime.date]

    def get_recommend(self, request: CircleGetRecommendRequest) -> CircleGetRecommendResult:
        # リポジトリに依頼するだけ
        recommend_circles = self._circle_repository.find_recommended(self._now)

        return CircleGetRecommendResult(recommend_circles)