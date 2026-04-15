---
publish: true
tags:
  - CPlusPlus
---
[[リテラル]]。ソースコード中に直接書かれた値を表す記法。

- [[整数リテラル（C++）]]
- 浮動小数点リテラル
- 文字リテラル
- [[文字列リテラル（C++）]]
- [[生文字列リテラル（C++）]]
- `true` / `false`
- `nullptr`

## 接尾辞

特定の接尾辞を用いることで、リテラルの型を指定したり絞り込んだりできる。
整数リテラルや浮動小数点リテラル、文字列リテラルでは、それぞれ使える接尾辞が異なる。

```c++
10.0 // double
10.0f // float
"hello"s // std::string
"hello"sv // std::string_view
// 一部を除いて、接尾辞の文字は大文字小文字を問わない
```

## 関連

- [[生文字列リテラル（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/introduction-to-literals-and-operators/
- https://www.learncpp.com/cpp-tutorial/literals/
