---
publish: true
tags:
  - CPlusPlus
---
# constexpr

[[コンパイル時評価]]できることを要求・保証するための指定子。
変数や関数などに付けて用いる。

## 変数

```cpp
constexpr double gravity { 9.8 };
```

`constexpr` 変数は、[[コンパイル時定数]]として扱われ、暗黙に [[const（C++）]] でもある。

## 関連

- [[constexpr関数]]
- [[即時関数]]

## 参考

- https://www.learncpp.com/cpp-tutorial/constexpr-functions/
