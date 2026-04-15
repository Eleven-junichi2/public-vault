---
publish: true
tags:
  - CPlusPlus
---
`std::exit`。`<cstdlib>` で提供される関数。
プログラムを通常終了させるために使う。

`main` から `return` する場合とは終了のしかたが異なる。
`return` では現在のスコープを抜ける過程でローカル変数が通常どおり破棄されるが、`std::exit` ではそのようなスコープ離脱による破棄は行われない。
ただし、[[atexit|std::atexit]] で登録した関数は、プログラム終了時に自動で実行される。

```cpp
#include <cstdlib>
#include <iostream>

int main()
{
    std::cout << 1 << '\n';
    std::exit(0);
    std::cout << 2 << '\n';
}
```

## 関連

- [[プログラムの終了]]
- [[atexit|std::atexit]]
- [[abort|std::abort]]

## 参考

- https://en.cppreference.com/w/cpp/utility/program/exit
