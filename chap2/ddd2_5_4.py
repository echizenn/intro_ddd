"""
2.5.4節のコードの説明
"""

# リスト2.44
def create_user(name: str):
    """
    入力値の確認を伴うユーザの作成処理

    Args:
        name (str): ユーザ名
    
    Returns: None

    Raises:
        ValueError: ユーザ名が3文字未満のとき
        
    Note:
        一見うまくいっているように見えるユーザ作成処理コード
        Userクラス実装していないので動かないです
    """
    if len(name) < 3: raise ValueError("ユーザ名は3文字以上です。")
    user: User = User(name)

# リスト2.45
def update_user(id: str, name: str):
    """
    ユーザ情報更新処理でも同様のコードを記述する

    Args:
        name (str): ユーザ名
    
    Returns: None

    Raises:
        ValueError: ユーザ名が3文字未満のとき

    Note:
        ユーザ情報更新処理でも同じ処理を反復していることを確認する
        Userクラス実装していないので動かないです
    """
    if len(name) < 3: raise ValueError("ユーザ名は3文字以上です。")
    user: User = User(name)

# リスト2.46
class UserName:
    """
    値オブジェクトにルールをまとめる

    Attributes:
        value (str): ユーザ名

    Raises:
        ValueError: ユーザ名が3文字未満のとき

    Note:
        ガード節を書いてオブジェクト作成時に不正な値ではないか確認する。
    """
    def __init__(self, value: str):
        if len(value) < 3: raise ValueError("ユーザ名は3文字以上です。")

        self.value = value

# リスト2.47
def create_user2(name: str):
    """
    値オブジェクトを利用した新規作成処理

    Args:
        name (str): 新規作成したいユーザ名
    
    Returns: None
    
    Note:
        不正な値かどうかの確認がまとまっていることを確認する。
        Userクラス実装していないので動かないです
    """
    user_name: UserName = UserName(name)
    user: User = User(user_name)

def update_user2(id: str, name: str):
    """
    値オブジェクトを利用した更新処理

    Args:
        id (str): 更新したいユーザid
        name (str): 更新したいユーザ名
    
    Returns: None

    Note:
        不正な値かどうかの確認がまとまっていることを確認する。
        Userクラス実装していないので動かないです
    """
    user_name: UserName = UserName(name)
