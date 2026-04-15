---
publish: true
tags:
  - CPlusPlus
---
文字や文字コード単位の値を表すためによく使われる[[整数型（C++）]]。
文字リテラルを格納できるが、`char`が符号付きか符号なしであるかは処理系依存である。

`char`は1文字を表す用途でよく使われる。
```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
    char ch { 'A' };
    std::cout << ch << '\n';
    return 0;
}
```

ASCIIでは英字が連続して割り当てられているため、`'A' + 32`のような計算で小文字に対応づけられる。
ただし、これは文字コードに依存する話であり、一般的な文字変換には向かない。

## リテラル

文字リテラルは `'a'` のように一重引用符で表す。

## 他のchar型

文字や文字コード単位を表す関連型。
- `char8_t`: `unsigned char`と同じサイズ
- `char16_t`: `std::uint_least16_t`と同じサイズ
- `char32_t`: `std::uint_least32_t`と同じサイズ
- `wchar_t`: 処理系依存のサイズを持つ

## 参考
