"""
6.4節のコードの説明
"""
import dataclasses

# リスト6.30
@dataclasses.dataclass
class LowCohesion:
    """
    凝集度が低いクラス

    Attributes:
        _value1 (int): フィールド
        _value2 (int): フィールド
        _value3 (int): フィールド
        _value4 (int): フィールド
    """
    _value1: int
    _value2: int
    _value3: int
    _value4: int

    def method_a(self) -> int:
        return self._value1 + self._value2
    
    def method_b(self) -> int:
        return self._value3 + self._value4

# リスト6.31
@dataclasses.dataclass
class HighCohesionA:
    """
    分離することで凝集度を高めたクラス

    Attributes:
        _value1 (int): フィールド
        _value2 (int): フィールド
    """
    _value1: int
    _value2: int

    def method_a(self) -> int:
        return self._value1 + self._value2


@dataclasses.dataclass
class HighCohesionB:
    """
    凝集度が低いクラス

    Attributes:
        _value3 (int): フィールド
        _value4 (int): フィールド
    """
    _value3: int
    _value4: int

    def method_b(self) -> int:
        return self._value3 + self._value4