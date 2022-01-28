"""
2.2.3節のコードの説明
"""
from ddd2_1 import FullName

# リスト2.13
def list2_13():
    """
    同じ種類の値同士の比較

    Args: None

    Returns: None

    Note:
        値は値を構成する属性によって評価される
    """
    print(0 == 0) # True
    print(0 == 1) # False
    print('a' == 'a') # True
    print('a' == 'b') # False
    print("hello" == "hello") # True
    print("hello" == "こんにちは") # False

# リスト2.14
def list2_14():
    """
    値オブジェクト同士の比較
    (メソッド実装してないので動かないです)

    Args: None

    Returns: None

    Note:
        値オブジェクトでの比較の例
    """
    name_a: FullName = FullName("masanobu", "naruse")
    name_b: FullName = FullName("masanobu", "naruse")

    # equalsメソッドがあるときの別個のインスタンス同士の比較
    print(name_a.equals(name_b)) # インスタンスを構成する属性が等価なのでTrue

# リスト2.15
def list2_15():
    """
    属性を取り出して比較

    Args: None

    Returns: None

    Note:
        やりがちだけどよくないオブジェクトの比較の例
    """
    name_a: FullName = FullName("masanobu", "naruse")
    name_b: FullName = FullName("john", "smith")

    compare_result: bool = (name_a.first_name == name_b.first_name
                            and name_a.last_name == name_b.last_name)

    print(compare_result)

# リスト2.16
def list2_16():
    """
    属性を取り出して比較する操作を数値にあてはめる
    (value属性は実際にはないので動かないです)

    Args: None

    Returns: None

    Note:
        属性を取り出すと違和感がある例
    """
    print(1.value == 0.value) # False ?

# リスト2.17
def list2_17():
    """
    値同士で比較する
    (equalsメソッドは実際にはないので動かないです)

    Args: None

    Returns: None

    Note:
        値同士の比較の仕方
    """
    name_a: FullName = FullName("masanobu", "naruse")
    name_b: FullName = FullName("john", "smith")

    compare_result: bool = name_a.equals(name_b)
    print(compare_result)

    # 演算子のオーバーライド機能を活用することも選択肢に入る
    # というよりpythonなら基本==で比較
    compare_result2: bool = name_a == name_b
    print(compare_result2)
