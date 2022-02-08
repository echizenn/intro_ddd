"""
13.1.1節のコードの説明
"""
import dataclasses
from typing import List

# リスト13.1
@dataclasses.dataclass
class Circle:
    """
    条件にしたがっているかを評価するふるまい
    """
    _owner: User
    _members: List[User]

    def is_full(self) -> bool:
        return self.count_members() >= 30

    def count_members(self) -> int:
        return len(self._members) + 1