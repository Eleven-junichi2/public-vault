---
publish: true
tags:
  - CPlusPlus
---
`std::is_constant_evaluated`。C++20で導入された、いまの評価が[[コンパイル時評価]]の文脈かどうかを真偽値で調べる標準関数。

関数そのものが「実行時の関数かコンパイル時の関数か」を調べるものではなく、その呼び出しが定数評価の中で行われているかを調べる。

```cpp
#include <type_traits>

constexpr int f()
{
    if (std::is_constant_evaluated())
        return 1;
    else
        return 2;
}
```

この例では、`f()`がコンパイル時評価される文脈では`1`を返し、そうでなければ`2`を返す。
