"""
7.4.1節のコードの説明
"""
from injector import Module

# リスト7.9
class ServiceLocator(Module):
    def configure(self, binder):
        # 変えたのはbindの引数toのみ
        # これで全体に変更が行き渡る
        binder.bind(IUserRepository, to=UserRepository)


# リスト7.10
# リスト7.11
# pythonの書き方だと外部から見えづらいことはない気がする