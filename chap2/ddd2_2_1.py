"""
2.2.1節のコードの説明
"""
from ddd2_1 import FullName

# リスト2.7
def list2_7():
    """
    値の変更をしている

    Args: None

    Returns: None

    Note:
        値が不変であるという主張に対する直感的な反例
    """
    greet: str = "こんにちは"
    print(greet) # こんにちは が表示される
    greet = "Hello"
    print(greet) # Hello が表示される

# リスト2.8
def list2_8():
    """
    「値の変更」を行う擬似コード
    (メソッド実装してないので動かないです)

    Args: None

    Returns: None

    Note:
        値を変更するとはどういうことか例を挙げている
    """
    greet: str = "こんにちは"
    greet.change_to("Hello") # このようなメソッドは本来存在しない
    print(greet) # Hello が表示される(change_toメソッドが存在すれば)

# リスト2.9
def list2_9():
    """
    値が変更できることを利用したコード
    (メソッド実装してないので動かないです)

    Args: None

    Returns: None

    Note:
        値の変更することで起こりうる面白い(違和感のある)例
        この例から、値は不変でないといけないことがわかる
    """
    "こんにちは".change_to("Hello") # このようなメソッドは本来存在しない
    print("こんにちは")  # Hello が表示される(2_8と同じ論理)

# リスト2.10
def list2_10():
    """
    一般的に見られる値の変更
    (メソッド実装してないので動かないです)

    Args: None

    Returns: None

    Note:
        システム固有の値を表す値オブジェクトは変更しないように警告している
    """
    full_name: FullName = FullName("masanobu", "naruse")
    full_name.change_last_name("sato")
