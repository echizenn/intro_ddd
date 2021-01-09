"""
2.3節のコードの説明
"""
from dataclasses import dataclass
from typing import Final # 再代入不可能という型ヒント

# リスト2.21
@dataclass
class FullName:
    """
    可能な限り値オブジェクトを適用したFullNameクラス

    Attributes:
        first_name (FirstName): 名を表すオブジェクト
        last_name (LastName): 姓を表すオブジェクト
    """
    first_name: Final[FirstName]
    last_name: Final[LastName]

# リスト2.22
@dataclass
class FirstName:
    """
    名を表す値オブジェクト

    Attributes:
        value (str): 名前
    """
    value: Final[str]

# リスト2.23
@dataclass
class LastName:
    """
    姓を表す値オブジェクト

    Attributes:
        value (str): 姓
    """
    value: Final[str]
