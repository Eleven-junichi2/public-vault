---
publish: true
tags:
  - CPlusPlus
---
C++では、[[文字列（C言語）]]に加えて、文字列を表現する[[クラステンプレート]]である `basic_string` が `<string>` ヘッダで提供される。
このクラステンプレートは文字型を[[テンプレートパラメータ]]で抽象化しており、通常は文字型として [[char型|char]] を使う[[型エイリアス（C++）]]である `std::string` がよく使われる。

## 長さの取得

- **符号なし**: `length()`/`size()`メンバ関数で取得できる。
- **符号付き**: `std::ssize()`で取得できる。（C++20）

UTF-8のように1文字が複数の`char`で表現される場合、`length()`や`size()`の結果は表示上の文字数と一致しないことがある。

`length()`と`size()`は機能・性能ともに同じである。

## 文字列の検索

- `find`メンバ関数で、最初に見つけた検索文字列の位置を取得できる。見つからなけえれば結果は無効な位置を表す`npos`メンバ[[定数（C++）]]の値になる。

例:
```cpp
#include <iostream>
#include <string>

int main()
{
  const std::string s("hello, world. welcome to C++ world.");
  const std::string find_word("world");
  std::string::size_type pos = s.find(find_word);
  while (pos != std::string::npos) {
    std::cout << pos << std::endl;
    pos = s.find(find_word, pos + find_word.length());
  }
}
```

## リテラル

`std::string_literals`を利用して接尾辞で`basic_string`の文字列リテラルを表現できる。

```cpp
#include <iostream>
#include <string>

int main()
{
    using namespace std::string_literals;

    std::cout << "foo\n";   // C文字列
    std::cout << "goo\n"s;  // std::basic_string

    return 0;
}
```

## パフォーマンスの考慮

- `basic_string` の初期化や値渡しでは、コピーが発生することがある。
- 読み取り専用で、参照先の文字列の寿命が十分長い場合は、[[string_view|std::string_view]]を使ってコピーを避けられる。

## 例

```cpp
#include <string>

int main()
{
    std::string emptyName {};
    std::string name { "Alex" };
    name = "Steve"; // 名前を変更。可変長なので最初の4文字より長くても格納できる
    
    return 0;
}
```

## 参考

- https://www.learncpp.com/cpp-tutorial/introduction-to-stdstring/
- https://note.com/morinokabu/n/n446ca3c3df31
- https://cpprefjp.github.io/reference/string/basic_string.html
