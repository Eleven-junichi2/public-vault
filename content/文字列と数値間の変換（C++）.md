---
publish: true
tags:
  - CPlusPlus
---

## 数値から文字列

### std::to_string

```cpp
#include <string>

int n = 42;
std::string s = std::to_string(n);  // "42"
```

```cpp
double d = 3.14;
std::string s = std::to_string(d);  // "3.140000"
```

## 文字列から数値

### std::stox

引数にとる文字列を数値型へ変換する関数が、各数値型ごとに**s**to**x**のような形式の命名で実装されている。

- [[int型（C++）]]: `std::stoi`
- [[浮動小数点数型（C++）#float]]: `std::stof`
- [[浮動小数点数型（C++）#double]]: `std::stod`
- 等

変換できない場合は例外`std::invalid_argument`が送出されるため処理を考慮する。

例:
```cpp
try {
    int n = std::stoi("abc");
} catch (const std::invalid_argument& e) {
    // 数値でない時の処理
}
```

## 関連

- [[高速な文字列と数値間の変換（C++）]]

## 参考

- https://cpprefjp.github.io/reference/string.html
- https://cpprefjp.github.io/reference/string/stoi.html
- https://cpprefjp.github.io/reference/string/to_string.html