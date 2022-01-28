"""
2.3節のコードの説明
"""
import dataclasses
from typing import Final # 再代入不可能という型ヒント

# リスト2.21
@dataclasses.dataclass(frozen=True)
class FullName:
    """
    可能な限り値オブジェクトを適用したFullNameクラス

    Attributes:
        _first_name (FirstName): 名を表すオブジェクト
        _last_name (LastName): 姓を表すオブジェクト

    Note:
        _first_nameと_last_nameはprivate変数なので
        そもそも外部には見せない想定。
    """
    _first_name: Final[FirstName]
    _last_name: Final[LastName]

# リスト2.22
@dataclasses.dataclass(frozen=True)
class FirstName:
    """
    名を表す値オブジェクト

    Attributes:
        _value (str): 名前
    """
    _value: Final[str]

# リスト2.23
@dataclasses.dataclass(frozen=True)
class LastName:
    """
    姓を表す値オブジェクト

    Attributes:
        _value (str): 姓
    """
    _value: Final[str]