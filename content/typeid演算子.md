---
publish: true
tags:
  - CPlusPlus
---
`typeid(型)`や`typeid(式)`によって型情報を得る[[演算子（C++）]]。
結果として`std::type_info`への参照が得られる。

`typeid(x).name()`で型名のような文字列を確認できることがあるが、その表現は処理系依存である。
