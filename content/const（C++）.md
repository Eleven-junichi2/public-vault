---
publish: true
tags:
  - CPlusPlus
---
`const`型修飾子。
対象を通じて値を変更できないようにするために用いられる。

```cpp
const double gravity { 9.8 };
int const sidesInSquare { 4 };
```

`const T` と `T const` は同じ意味である。

定数変数は、通常は[[宣言（C++）]]時に[[初期化（C++）]]する。
一般的には `const T` の形で書かれることが多い。
