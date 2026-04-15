---
publish: true
tags:
  - CPlusPlus
---
`std::string_view`。`<string_view>`ヘッダで提供される。
文字列の[[所有権]]を保持せず、コピーではなく参照を保持して文字列を扱う。
コピーせずに文字列へ読み取り専用アクセスできるため、コピーによるコストを避けたいときに利用される。
`std::string`、文字列リテラル、他の[[string_view]]などで初期化できる。

暗黙的に`std::string`には変換されない。

用途：関数の文字列を受け取る引数の型。

## ダングリング・ビュー

[[string_view]]への新しい文字列の割り当ては、その文字列へのviewに切り替えられ、以前の文字列とは無関係。文字列が変更・破壊された先へのviewは**ダングリング・ビュー（Dangling View）** であり、未定義動作を起こすため注意が必要。特に、返り値としての扱いでこの問題を誤ってプログラムしやすい。

- [[文字列（C言語）|C言語スタイルの文字列]]のリテラルに対しては、この文字列はプログラム全体に存在するため、問題を回避しやすい。
- ローカル変数の[[文字列（C++）|std::string]]を指す `std::string_view` を返すと、関数終了時に参照先が破壊されて問題が起きる。

## View操作関数（View modification functions）

元の文字列を変更せず、参照する内容の範囲を操作できる。

| **関数**               | **動作**                             |
| -------------------- | ---------------------------------- |
| `remove_prefix(n)`   | 先頭から `n` 文字分、参照範囲を減らす。             |
| `remove_suffix(n)`   | 末尾から `n` 文字分、参照範囲を減らす。             |
| `substr(pos, count)` | `pos` から `count` 文字分の新しい View を返す。 |

## リテラル

`"文字列"sv`
`sv` は `std::string_view_literals` で提供される接尾辞である。

```cpp
#include <iostream>
#include <string_view>

int main()
{
    using namespace std::string_view_literals;

    std::cout << "moo\n"sv;

    return 0;
}
```
