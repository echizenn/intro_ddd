"""
2.2.3節のコードの説明
FullNameクラスの構造を変える例
"""
from __future__ import annotations # これで自己クラスを型ヒントで使える
import dataclasses

# リスト2.20
"""
dataclassを用いることで、自動で
__init__, __repr__, __eq__
を生成してくれるので、equalメソッドの実装は不要だが、
オーバーライド可能なので、学習のため実装する。
"""
@dataclasses.dataclass
class FullName:
    """
    氏名を表現するクラス

    Attributes:
        first_name (str): 名
        last_name (str): 姓
    """
    first_name: str
    last_name: str
    middle_name: str # リスト2.20で追加

    def __eq__(self, other: FullName) -> bool:
        """
        FullNameインスタンス同士を比較する

        Args:
            other (FullName): 比較相手
        
        Returns:
            bool: 同値性をもつ場合True

        Note:
            修正が一箇所だけで済むことを確認する
        """
        if type(self) != type(other): return False # 型が異なるときはFalseを返す
        return (self.first_name == other.first_name
                and self.last_name == other.last_name
                and self.middle_name == other.middle_name) # リスト2.20でこの行追加

# リスト2.19
def list2_19(name_a: FullName, name_b: FullName) -> bool:
    compare_result: bool = (name_a.first_name == name_b.first_name
                            and name_a.last_name == name_b.last_name
                            and name_a.middle_name == name_b.middle_name)