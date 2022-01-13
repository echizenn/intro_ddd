"""
12.4節のコードの説明
"""
import dataclasses
from typing import List


# リスト12.22
@dataclasses.dataclass
class Circle:
    """
    30ではなく29が現れている
    """
    _owner: User
    _members: List[User]

    def is_full(self) -> bool:
        return len(self._members) >= 29