---
publish: true
tags:
  - CPlusPlus
---
`const std::string&` は、`std::string` を読み取り専用で受け取る参照である。
`std::string_view` は、`std::string`、文字列リテラル、C文字列などを柔軟に受け取れる非所有の文字列ビューである。

多くの場合、文字列を読み取り専用で受け取る引数には `std::string_view` が向いている。
これは、より広い種類の文字列引数を効率よく受け取れるためである。

一方で、関数内で C文字列や `std::string` を要求する別の関数をそのまま呼びたい場合は、`const std::string&` のほうが扱いやすいことがある。
`std::string_view` はヌル終端を保証せず、`std::string` への変換も効率がよいとは限らないためである。

`std::string_view` を使う場合は、参照先の[[生存期間（C++）]]にも注意が必要である。

## 参考

- [LearnCpp: Pass by const lvalue reference](https://www.learncpp.com/cpp-tutorial/pass-by-const-lvalue-reference/)
