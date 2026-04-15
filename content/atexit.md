---
publish: true
tags:
  - CPlusPlus
---
`<cstdlib>` で提供される関数。
プログラムの通常終了時に呼びたい後始末関数を登録するために使う。

`main` からの `return` や [[exit|std::exit]] による終了時に呼ばれる。

```cpp
#include <cstdlib>
#include <iostream>

void cleanup()
{
    std::cout << "cleanup\n";
}

int main()
{
    std::atexit(cleanup);
    std::cout << 1 << '\n';
}
```

## 関連

- [[プログラムの終了]]
- [[exit|std::exit]]

## 参考

- https://en.cppreference.com/w/cpp/utility/program/atexit
