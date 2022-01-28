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


# Pythonでの実装ルール
## chap2
### 値オブジェクト  
値オブジェクトの大事な点としては、attributesが変更できない点  
これをPython上で強制するには、namedtupleを用いる方法とdataclasses.dataclass(frozen=True)を用いる方法がある。できることはほとんどどちらも同じであり、後者の方が変更が楽な(今後もdataclassを使うことが多い)ため、基本的にはdataclasses.dataclass(frozen=True)を用いることにする。  
例：
```Python
import dataclasses

@dataclasses.dataclass(frozen=True)
class ValueObject:
    value: int
```

一方、上記の方法では、自作の__init__を利用することができない(代入不可能ですよとエラーが出る)ので、ガード節(文字数の条件など)を記入したい場合は、typingモジュールのFinalで型アノテーションを行い、__init__以降では再代入できないことを明記する。  
例：
```python
from typing import Final

class ValueObject:
    def __init__(self, value: str):
        # ArgumentExceptionは自分で実装する
        if len(value) <= 2: raise ArgumentException("3文字以上である必要があります。", str(value))
        self.value: Final[str] = value