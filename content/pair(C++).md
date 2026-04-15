---
publish: true
tags:
  - CPlusPlus
---
`std::pair`。`<utility>`ヘッダで提供される。
二つの値をひとまとめに扱うのに便利な[[クラステンプレート]]。
要素は `first` と `second` という名前のメンバで保持される。

```cpp
#include <iostream>
#include <utility>

int main()
{
    std::pair<int, double> p1{ 1, 2.3 };
    std::cout << p1.first << ", " << p1.second << '\n';

    std::pair p2{ 4.5, 6 };
    std::cout << p2.first << ", " << p2.second << '\n';
}
```

