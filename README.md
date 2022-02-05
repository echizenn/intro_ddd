# intro_ddd
ドメイン駆動設計入門のPythonでのサンプルコードです。

作成していない仮想のメソッドやクラスを利用したりしているので
動かないコードもあります。

ドキュメントコメントはGoogleスタイルで書いている。
- https://chromium.googlesource.com/chromiumos/docs/+/master/styleguide/python.md
- https://www.memory-lovers.blog/entry/2019/01/10/004107

# それぞれの章の使い分け

- [chap2](#chap2)  
値オブジェクト: 変更のないシステム固有の値を定義するのに使う(ユーザIDとか)  

- [chap3](#chap3)  
エンティティ: 可変であり、同一性によって区別される値を定義するのに使う(ユーザとか)  

- [chap4](#chap4)  
ドメインサービス: 異なるエンティティや値オブジェクトを参照するふるまいを定義するのに使う

- [chap5](#chap5)  
リポジトリ: ドメインオブジェクト(値オブジェクトやエンティティ)の永続化や再構築を行う

- [chap6](#chap6)  
アプリケーションサービス: ドメインではなく、アプリケーションのためのサービスを記述する


# Pythonでの実装ルール
## chap2
### 値オブジェクト  
値オブジェクトの大事な点としては、attributesが変更できない点  
これをPython上で強制するには、namedtupleを用いる方法とdataclasses.dataclass(frozen=True)を用いる方法がある。できることはほとんどどちらも同じであり、後者の方が変更が楽な(今後もdataclassを使うことが多い)ため、基本的にはdataclasses.dataclass(frozen=True)を用いることにする。  
例：
```python
import dataclasses
from typing import Final


@dataclasses.dataclass(frozen=True)
class ValueObject:
    value: Final[int]
```

一方、上記の方法では、自作の\_\_init\_\_関数を利用することができない(代入不可能ですよとエラーが出る)ので、ガード節(文字数の条件など)を記入したい場合は、\_\_post_init\_\_関数を用いる。   
例：
```python
import dataclasses
from typing import Final


@dataclasses.dataclass(frozen=True)
class ValueObject:
    value: Final[str]

    def __post_init__(self):
        # ArgumentExceptionは自分で実装する
        if len(self.value) < 3: raise ArgumentException("3文字以上である必要があります。", str(self.value))
```

## chap3
### エンティティ  
エンティティでは、比較に用いるidなどの変数は不変性を持ち、年齢などの変わりうる変数は適切に変更できる必要がある。  
これをPythonで実装するには、不変性を持つ変数をFinalで型アノテーションすればよい。  
また、比較対象となる変数に関して、\_\_eq\_\_関数を実装する。  
例：
```python
# 自己クラスを型アノテーションで使えるようにする
from __future__ import annotations
import dataclasses
from typing import Final

@dataclasses.dataclass
class Entity:
    _id: Final[Id]
    _age: int

    @property
    def id(self) -> Id:
        return self._id

    @property
    def age(self) -> int:
        return self._age

    def __eq__(self, other: Entity) -> bool:
        """
        他のオブジェクトとの比較

        Args:
            other (Entity): 比較相手のEntityオブジェクト
        
        Returns:
            bool: 同一性を持つか否か
        """
        if type(self) != type(other): return False
        return self._id == other._id
```

## chap4
### ドメインサービス
複数のドメインの間で決まったやり取りがある場合に用いる。  
どこまでドメインサービスに含めるかはかなり議論があるっぽい。  
プロジェクトによってある程度は統一し、適宜自分で考える必要がありそう。  
実装上の注意点は特になく、通常通りクラスを定義すれば良い。

## chap5
### リポジトリ
ドメインオブジェクト(値オブジェクトやエンティティ)の永続化や再構築を行うものなので、役割はわかりやすい。   
基本的に、クラスのAttributeとして、データベースの情報やファイルの情報を持ち、メソッドはドメインオブジェクトが引数となる。  
例：
```python
from abc import ABCMeta, abstractmethod
import dataclasses
from typing import Final


class InterfaceRepository(metaclass=ABCMeta):
    """
    リポジトリのインターフェイス
    (特定の技術の)リポジトリへの依存をなくすために、インターフェイスを定義する
    """
    @abstractmethod
    def find(self, id_: Id) -> Entity:
        pass


@dataclasses.dataclass(frozen=True)
class Repository(InterfaceRepository):
    """
    なんらかの技術(MySQLなど)を用いたリポジトリ
    """
    _db: Final[Database]

    def find(self, id_: Id) -> Entity:
        target = self._db["Entity"].find_one(id_) # イメージでのコードなので、詳細はchap5フォルダを参考してください
        if target is None: return None
        return Entity(Id(target._id), int(target._age))
```

## chap6
### アプリケーションサービス
クライアントに必要なサービスを記述する。  
Attributesはドメインサービスやレポジトリを含むことが多い。  
メソッドの引数にはコマンドオブジェクトを利用することで、interfaceを変更する必要が減る。  
メソッドの返り値としてデータ転送用オブジェクトを用いることで、ドメインが外部に流出することを防ぐ。  

例：
```python
import dataclasses
from typing import Final

@dataclasses.dataclass(frozen=True)
class ApplicationService:
    _repository: Final[InterfaceRepository]

    def register(self, command: EntityRegisterCommand):
        entity = Entity(Id(command.id), command.age)
        self._user_repository.save(entity)
```

### コマンドオブジェクト
上記アプリケーションサービスのメソッドの引数に用いるオブジェクト  
基本的にコンストラクタ(\_\_init\_\_)とgetterだけ用意すれば良い。  

例：
```python
@dataclasses.dataclass(frozen=True)
class EntityRegisterCommand:
    id: Final[str]
    age: Final[int]
```

### データ転送用オブジェクト
上記アプリケーションサービスのメソッドの返り値に用いるオブジェクト  
コマンドオブジェクトと同様にコンストラクタとgetterだけ用意すれば良い。  
コンストラクタの引数をドメインオブジェクトにすると、ドメインの変更に強くなる。  

例：
```python
@dataclasses.dataclass(frozen=True)
class EntityData:
    def __init__(self, entity: Entity):
        self.id = entity.id.value
        self.age = entity.age
```