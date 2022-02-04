"""
5.8.1節のコードの説明
"""
from abc import ABCMeta, abstractmethod

from chap4.ddd4_4_1 import User, UserId, UserName


class IUserRepository(metaclass=ABCMeta):
    """
    Userクラスのリポジトリインターフェース
    """

    # リスト5.22
    @abstractmethod
    def save(self, user: User):
        """
        永続化を行うふるまい
        名前はstoreとかでも良い

        Args:
            user (User): 保存したいUserインスタンス

        Returns: None
        """
        pass

    # リスト5.23
    @abstractmethod
    def update_name(self, id: UserId, name: UserName):
        """
        ユーザ名を更新する
        更新項目を引き渡す更新処理(悪い例)
        永続化を行うオブジェクトを引数にとっていないのがおかしい

        Args:
            id (UserId): 更新したいユーザのid
            name: (UserName): 更新したいユーザ名
        
        Returns: None
        """
        pass

    # リスト5.24
    @abstractmethod
    def update_email(self, id: UserId, mail: Email):
        """
        メールアドレスを更新する
        更新項目を引き渡す更新処理(悪い例)
        永続化を行うオブジェクトを引数にとっていないのがおかしい
        このようにメソッドが乱立してしまう

        Args:
            id (UserId): 更新したいユーザのid
            name: (Email): 更新したいメールアドレス
        
        Returns: None
        """
        pass

    # リスト5.25
    @abstractmethod
    def delete(self, name: User):
        """
        ユーザの削除
        破棄を行うふるまいを定義したリポジトリ

        Args:
            user (User): 削除したいユーザ
        
        Returns: None
        """
        pass