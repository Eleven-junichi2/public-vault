---
publish: true
tags:
  - CPlusPlus
---

C++17では、`<charconv>`ヘッダで高速な文字列・数値変換が提供される。
ロケール非依存、動的メモリ確保なし、例外なしで変換できる。

[[文字列と数値間の変換（C++）]]で扱う`std::to_string`や`std::stoi`系は使いやすい一方、こちらはより低レベルだが高速な変換方法である。

## 数値から文字列

### `std::to_chars`

数値を指定した文字バッファ範囲に書き込む関数。

```cpp
#include <charconv>
#include <iostream>

int main()
{
    char buffer[16] {};
    int value { 12345 };

    auto [ptr, ec] { std::to_chars(buffer, buffer + 16, value) };

    if (ec == std::errc{}) {
        std::cout.write(buffer, ptr - buffer);
        std::cout << '\n';
    }
}
```

`ptr`は書き込みが終わった位置を指し、変換結果は`[buffer, ptr)`の範囲に入る。
自動では[[ヌル終端文字列|ヌル終端]]されないため、必要なら自分で終端文字を追加する。

`std::to_string`は`std::string`を返して扱いやすいが、`std::to_chars`はバッファを直接扱う代わりに高速である。
整数だけでなく浮動小数点数も対象だが、書式指定や処理系差の詳細は別途確認が必要である。

## 文字列から数値

### `std::from_chars`

文字列の範囲`[first, last)`を数値へ変換する関数。

```cpp
#include <charconv>
#include <iostream>

int main()
{
    const char text[] { "12345abc" };
    int value {};

    auto [ptr, ec] { std::from_chars(text, text + 8, value) };

    if (ec == std::errc{}) {
        std::cout << value << '\n';
    }
}
```

`ptr`は変換に使われなかった最初の文字を指す。
変換に失敗した場合も例外は投げず、`ec`で結果を確認する。

- 数値として読めない場合は `std::errc::invalid_argument`
- 範囲外の値なら `std::errc::result_out_of_range`

`std::stoi`系と違い、先頭の空白は読み飛ばさず、`+`も受け付けない。
また、`0x`のような接頭辞も自動では解釈しない。
失敗した場合、変換先の値は変更されない。

## 補足

- `to_chars` / `from_chars` は、null終端文字列そのものではなく範囲`[first, last)`を扱う
- バッファを自分で用意する必要がある
- 書式指定や入力の柔軟さは、`iostream`や`std::stoi`系より限定的である
- JSONやCSVのような、機械が生成・消費するテキストの変換と相性がよい

## 関連

- [[文字列と数値間の変換（C++）]]

## 参考

- https://cpprefjp.github.io/reference/charconv.html
