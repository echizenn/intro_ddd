"""
3.2.1節のコードの説明
"""

# リスト3.2
class User:
    """
    可変なオブジェクトに変化させる

    Attributes:
        _name (str): ユーザ名
    """
    def __init__(self, name):
        self.change_name(name)

    @name.setter
    def name(self, name: str):
        """
        外部からnameを変更できるようにする

        Args:
            name (str): 新しいユーザ名
        
        Returns: None

        Note:
            ユーザ名は3文字以上
        """
        self.change_name(name)
    
    def change_name(self, name: str):
        """
        ユーザ名を変える

        Args:
            name (str): 新しいユーザ名
        
        Returns: None

        Raises:
            ValueError: 新しいユーザ名が3文字未満のとき
        
        Note:
            ユーザ名は3文字以上です
            振る舞いでユーザ名が変更できるようになっている。
        """
        if len(name) < 3: raise ValueError("ユーザ名は3文字以上です。")
        self._name: str = name