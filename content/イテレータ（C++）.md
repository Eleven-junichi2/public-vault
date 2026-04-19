---
publish: true
tags:
  - CPlusPlus
---
[[コンテナ（C++）]]や配列の要素列を順にたどるためのオブジェクト。

標準ライブラリの[[コンテナ（C++）]]は、それぞれイテレータを提供している。
`begin()`は先頭要素を指すイテレータを返し、`end()`は末尾の次を指す終端イテレータを返す。
`std::begin`や`std::end`などの補助関数は`<iterator>`ヘッダで提供される。

```cpp
#include <array>
#include <iostream>
#include <iterator>

int main()
{
    std::array array{ 1, 2, 3 };

    // 要素の先頭と末尾を指すイテレータ
    auto begin{ std::begin(array) };
    auto end{ std::end(array) };

    for (auto p{ begin }; p != end; ++p) // ++ で次の要素を指す
    {
        std::cout << *p << ' '; // 間接参照で要素を取得
    }
    std::cout << '\n';

    return 0;
}
```

多くのイテレータは等値比較（`==`, `!=`）で終端かどうかを判定できる。
一方、`<` や `>` のような関係演算子が使えるとは限らないため、汎用的なループでは `!= end` という形がよく使われる。

## よく使う操作

- `*it`: イテレータが指す要素を参照する
- `++it`: 次の要素へ進める
- `it == end()が返す終端イテレータ`, `it != end()が返す終端イテレータ`: 走査が終わったかを判定する

## erase()との関係

一部のコンテナの`erase()`メンバ関数は、指定したイテレータが指す要素を削除し、その次の要素を指すイテレータを返す（なければ`end()`を返す）。
要素削除中に走査を続けるときによく使う。

## ダングリングイテレータ

イテレータが指していた要素が削除されたり、コンテナの内部再配置によって要素の位置が変わったりすると、そのイテレータは無効になることがある（[[イテレータの無効化]]）。
このような無効なイテレータにアクセスすると[[未定義動作]]になる。

たとえば `std::vector` では、再割り当てや要素削除によって、既存のイテレータが無効化されることがある。

## 関連

- [[イテレータの無効化]]

## 参考

- https://www.learncpp.com/cpp-tutorial/introduction-to-iterators/
- https://cpprefjp.github.io/reference/iterator.html
