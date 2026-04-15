---
publish: true
tags:
  - CPlusPlus
---
`std::common_type`。複数の[[型（C++）]]から、共通に扱える型を得るための型特性。
`std::common_type_t<T1, T2>`の形で簡潔に書ける。

```cpp
std::common_type_t<int, double> x; // double
```

[[通常の算術変換]]と近い結果になることはあるが、`std::common_type`は標準ライブラリの型特性であり、式の評価前に実際に行われる変換規則そのものではない。
