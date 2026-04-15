---
publish: true
tags:
  - CPlusPlus
---
`getline` には、 `std::getline` と、`std::istream` のメンバ関数 `getline` がある。
名前は同じでも用途が少し違う。

## `std::getline`

`std::getline(std::istream&, std::string&, 区切り文字)` は、文字列を 1 行単位で受け取るときに使う。
改行までを読み取り、区切り文字自体は結果に含めない。

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string line {};
    std::getline(std::cin, line);
    std::cout << line << '\n';
}
```

## `std::istream::getline`

`std::cin.getline(char*, size)` は、C 文字列バッファへ読み込むメンバ関数。
固定長バッファを使うときに現れるが、`std::string` を使える場面では `std::getline` の方が扱いやすい。

```cpp
#include <iostream>

int main()
{
    char buffer[256] {};
    std::cin.getline(buffer, 256);
    std::cout << buffer << '\n';
}
```

## `get()` との違い

`std::istream::get()` も非書式化入力関数だが、こちらは区切り文字を残したまま止まる。
一方、`getline()` は区切り文字を読み取って捨てる。

この違いのため、同じ入力に対して `get()` を続けて呼ぶと、前回残った改行にすぐ当たって空文字列になることがある。
行単位で自然に読み進めたいなら、通常は `getline()` の方が扱いやすい。

## 違い

| 項目         | `std::getline` | `std::istream::getline` |
| ---------- | -------------- | ----------------------- |
| 主な格納先      | `std::string`  | `char[]`                |
| 改行の扱い      | 読み取って捨てる       | 読み取って捨てる                |
| `gcount()` | 更新しない          | 更新する                    |
| 典型用途       | 1 行文字列の取得      | 固定長バッファへの読み込み           |

## `>>` と混ぜるときの注意

[[抽出演算子]] `>>` の直後は、入力を確定した改行がストリームに残ることがある。
そのまま `std::getline` を呼ぶと、空文字列を読んだように見えることがある。

対策は次のどちらか。

- `std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');` で残りを捨てる
- `std::getline(std::cin >> std::ws, line);` のように `std::ws` で先頭空白を飛ばす

## `gcount()`

`gcount()` は、直前の非書式化入力関数が何文字読んだかを返す。
`std::istream::getline` や `ignore` の結果確認には使えるが、自由関数の `std::getline` では使わない。

## 関連

- [[標準入力（C++）]]
- [[抽出演算子]]
- [[非書式化入力関数]]
- [[マニピュレータ（C++）]]
- [[ストリーム状態と入力検証（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/input-with-istream/
- https://en.cppreference.com/w/cpp/string/basic_string/getline
- https://en.cppreference.com/w/cpp/io/basic_istream/getline
