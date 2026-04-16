---
tags:
  - CPlusPlus
publish: true
---
Tuple。異なる型を格納できる固定長のコレクション。C++では、`<tuple>`ヘッダで提供される`std::tuple`を利用することができる。

例:
```cpp
#include <iostream>
#include <tuple>
#include <string>

int mani()
{
    std::tuple<int, char, std::string> t = std::make_tuple(1, 'a', "hello");
    int& i = std::get<0>(t); // 位置を指定して取得
    std::cout << i << std::endl;
    std::string& s = std::get<std::string>(t); // 型を指定して取得
    std::cout << s << std::endl;
    return 0;
}
```

例（C++17）:
```cpp
#include <iostream>
#include <tuple>
#include <string>

// 関数から複数の値を返す
std::tuple<int, char, std::string> f()
{
  // std::make_tuple()はほとんどの状況で必要ない
  return {1, 'a', "hello"};
}

int main()
{
  // 構造化束縛でタプルを分解して、それぞれの要素を代入
  auto [a, b, c] = f();

  std::cout << a << std::endl;
  std::cout << b << std::endl;
  std::cout << c << std::endl;
}
```

## 参考

- https://cpprefjp.github.io/reference/tuple/tuple.html