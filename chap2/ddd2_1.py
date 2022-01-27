"""
2.1節のコードの説明
"""
import dataclasses
from typing import List

# リスト2.1
def list2_1():
    """
    プリミティブな値で「氏名」を表示する

    Args: None

    Returns: None

    Note:
        Pythonの基本文法のみを用いて氏名をもっとも簡単に表示する
    """
    fullname: str = "naruse masanobu"
    print(fullname) # naruse masanobuが表示される

# リスト2.2
def list2_2():
    """
    姓だけを表示する

    Args: None

    Returns: None

    Note:
        split関数を用いて姓だけを表示する
    """
    fullname: str = "naruse masanobu"
    tokens: List[str] = fullname.split() # ["naruse", "masanobu"]という配列にしている
    last_name: str = tokens[0]
    print(last_name) # naruseが表示される

# リスト2.3
def list2_3():
    """
    うまく姓を表示できないパターン

    Args: None

    Returns: None

    Note:
        リスト2.2では正しく姓を取り出すロジックを書けていないという例
    """
    fullname: str = "john smith"
    tokens: List[str] = fullname.split() # ["john", "smith"]という配列に
    last_name: str = tokens[0]
    print(last_name) # johnが表示される

# リスト2.4
@dataclasses.dataclass
class FullName(object):
    """
    氏名を表現するクラス

    Attributes:
        first_name (str): 名
        last_name (str): 姓
    """
    first_name: str
    last_name: str

# リスト2.5
def list2_5():
    """
    FullNameクラスのlast_nameプロパティを利用する

    Args: None

    Returns: None

    Note:
        クラスを作成することで、正しく姓を取れるという例
    """
    full_name: FullName = FullName("masanobu", "naruse")
    print(full_name.last_name)

# リスト2.6
def list2_6():
    """
    確実に姓を表示できる

    Args: None

    Returns: None

    Note:
        john smithさんでも正しく姓を取れる確認
    """
    full_name: FullName = FullName("john", "smith")
    print(full_name.last_name) # smithが表示される
