---
publish: true
tags:
  - CPlusPlus
---
[[宣言（C++）]]や[[文（プログラミング）]]などに付けて、そのコードをどう扱うかについての追加情報を[[コンパイラ]]に伝えるための書き方。
属性は`[[attr]]`のように二重角括弧で囲んで指定する。

例:
```cpp
[[nodiscard]] int f();
[[maybe_unused]] int x;
```

## 参考

- https://cpprefjp.github.io/lang/cpp11/attributes.html
