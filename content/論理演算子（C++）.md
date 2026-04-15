---
publish: true
tags:
  - CPlusPlus
---
[[bool型（C++）]]としての真偽を組み合わせる[[演算子（C++）]]。

代表例:

- AND: `&&`
- OR: `||`
- NOT: `!`

`&&` と `||` は短絡評価を行う。
たとえば `a && b` では、`a` が `false` なら `b` は評価されない。

## 参考

- https://eel.is/c++draft/expr.log.and
- https://eel.is/c++draft/expr.log.or
