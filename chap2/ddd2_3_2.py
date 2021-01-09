"""
2.3節のコードの説明
"""
import re

# リスト2.24
class FullName:
    """
    FullNameでルールを担保する

    Attributes:
        first_name (str): 名
        last_name (str): 姓

    Raises:
        ValueRrror: 姓名にアルファベット以外が使われているとき
    """
    def __init__(self, first_name: str, last_name: str):
        if not self.validate_name(first_name):
            raise ValueError("許可されていない文字が使われています")
        if not self.validate_name(last_name):
            raise ValueError("許可されていない文字が使われています")

        self.first_name: str = first_name
        self.last_name: str = last_name

    @staticmethod
    def validate_name(value: str) -> bool:
        # アルファベットに限定する
        return re.fullmatch('[a-zA-Z]+', value)
