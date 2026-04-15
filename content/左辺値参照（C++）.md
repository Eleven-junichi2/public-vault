---
publish: true
tags:
  - CPlusPlus
---
`int&` や `float&` のように `&` を使って表す参照型。
主に名前を持つ[[オブジェクト（C++）]]に[[束縛]]され、[[オブジェクト（C++）]]のエイリアスとして振る舞う。
参照は[[オブジェクト（C++）]]ではないので、[[オブジェクト（C++）]]が要求される場面ではそのまま使えない。
参照を通した操作は、参照先のオブジェクトに反映される。

参照(例:`int&`)を指定する型は、参照型と呼ばれる。

参照は必ず[[初期化（C++）]]される必要がある。
初期化によって参照をオブジェクトに関連づけることを[[束縛]]と呼ぶ。

参照は、いったん[[束縛]]されると別のオブジェクトへ付け替えることはできない。

参照と参照先の[[生存期間（C++）]]は独立している。

```cpp
#include <iostream>

float value { 8.9f };
float& accl { value }; // value への参照
// `float &accl` と書いても意味は同じ
std::cout << accl << '\n';
accl = 2.2f; // accl を通して value の値を変更
std::cout << value << '\n';
```

## 参考

- https://www.learncpp.com/cpp-tutorial/lvalue-references/
