"""
2.2.3節のコードの説明
FullNameクラスを作り直すので新しいファイルにした
"""
from __future__ import annotations # これで自己クラスを型ヒントで使える
import dataclasses

# リスト2.18
"""
Pythonでの簡単な値オブジェクトの実装は
NamedTupleを使うのがいいと思われる(getを実装する場合)。
Immutableということを伝えらえる上、
値の比較もインスタンス変数同士での比較をしてくれる。
ここでは学習のため__eq__関数を実装している。

getを実装しない場合は、dataclass(frozen=True)で
private変数として実装するのがいいと思われる。
"""
@dataclasses.dataclass
class FullName:
    """
    氏名を表現するクラス

    Attributes:
        first_name (str): 名
        last_name (str): 姓
    """
    _first_name: str
    _last_name: str

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def __eq__(self, other: FullName) -> bool:
        """
        FullNameインスタンス同士を比較する

        Args:
            other (FullName): 比較相手
        
        Returns:
            bool: 同値性をもつ場合True
        """
        if type(self) != type(other): return False # 型が異なるときはFalseを返す
        return (self._first_name == other._first_name
                and self._last_name == other._last_name)
