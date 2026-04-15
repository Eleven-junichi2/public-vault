---
publish: true
tags:
  - CPlusPlus
---
`<cstdlib>` で提供される関数。
プログラムを異常終了させるために使う。

通常終了とは異なり、[[atexit|std::atexit]] で登録した関数は呼ばれない。

```cpp
#include <cstdlib>

int main()
{
    std::abort();
}
```

## 関連

- [[プログラムの終了]]
- [[exit|std::exit]]
- [[atexit|std::atexit]]

## 参考

- https://en.cppreference.com/w/cpp/utility/program/abort
