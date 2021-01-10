# intro_ddd
ドメイン駆動設計入門のPythonでのサンプルコード

作成していない仮想のメソッドやクラスを利用したりしているので
動かないコードもあります。

ドキュメントコメントはGoogleスタイルで書いている。
- https://chromium.googlesource.com/chromiumos/docs/+/master/styleguide/python.md
- https://www.memory-lovers.blog/entry/2019/01/10/004107

# それぞれの章の使い分け
2章値オブジェクト: 変更のないシステム固有の値を定義するのに使う(ユーザIDとか)
3章エンティティ: 可変であり、同一性によって区別される値を定義するのに使う(ユーザとか)
4章ドメインサービス: 異なるエンティティや値オブジェクトを参照するふるまいを定義するのに使う