"""
13.2.2節のコードの説明
"""
from abc import ABCMeta, abstractmethod
import dataclasses
import datetime
from typing import Any, Final, List


# リスト13.14
class ISpecification(metaclass=ABCMeta):
    """
    仕様のインターフェース
    """
    @abstractmethod
    def is_satisfied_by(self, value: Any) -> bool:
        pass


class CircleRecommendSpecification(ISpecification):
    """
    仕様の実装クラス
    """
    pass

# リスト13.15
class ICircleRepository(metaclass=ABCMeta):
    """
    リポジトリは仕様のインターフェースを受け取り結果セットを返す
    """
    @abstractmethod
    def find(self, specification: ISpecification) -> List[Circle]:
        pass

# リスト13.16
@dataclasses.dataclass
class CircleApplicationService:
    """
    リスト13.14を利用してお勧めサークルを探す
    """
    _circle_repository: Final[ICircleRepository]
    _now: Final[datetime.date]

    def get_recommend(self, request: CircleGetRecommendRequest) -> CircleGetRecommendResult:
        circle_recommend_specification = CircleRecommendSpecification(self._now)
        # リポジトリに仕様を引き渡して抽出(フィルタリング)
        recommend_circles = self._circle_repository.find(circle_recommend_specification)[:10]

        return CircleGetRecommendResult(recommend_circles)