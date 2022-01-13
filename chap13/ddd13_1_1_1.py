"""
13.1.1節のコードの説明
"""

# リスト13.1
class Circle:
    """
    条件にしたがっているかを評価するふるまい
    """
    def is_full(self) -> bool:
        return self.count_members() >= 30