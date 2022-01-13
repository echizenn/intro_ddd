"""
12.4節のコードの説明
"""
import dataclasses
from typing import List


# リスト12.23
@dataclasses.dataclass
class Circle:
    """
    サークルのオーナーとメンバーの定義
    """
    _owner: User
    _members: List[User]

    def is_full(self) -> bool:
        return self.count_members() >= 30

    def count_members(self) -> int:
        return len(self._members) + 1