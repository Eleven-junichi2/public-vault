---
publish: true
tags:
  - CPlusPlus
---
**p**ure **rvalue**。抽象化して捉えると、概ね**値そのものを表す式**である[[値のカテゴリ（C++）]]。
- [[アイデンティティ（C++）]]を持たない
- [[ムーブ]]元になれる

具体的には、たとえば以下のような式を指す:
- 組み込み[[演算子（C++）]]の[[オペランド]]の値を計算する式
- [[オブジェクト（C++）]]を初期化する式

[[prvalue]]が[[実体（C++）]]のある[[オブジェクト（C++）]]として扱われる必要がある文脈では、[[一時オブジェクト（C++）]]が生成され、その一時オブジェクトを表す[[xvalue]]が得られる（temporary materializationと呼ばれる挙動。）

## 関連

- [[rvalue]]
- [[値のカテゴリ（C++）]]

## 参考

- https://cpprefjp.github.io/lang/cpp11/rvalue_ref_and_move_semantics.html
- https://en.cppreference.com/w/cpp/language/value_category.html#Move-eligible_expressions