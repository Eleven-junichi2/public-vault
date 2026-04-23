---
tags:
  - CPlusPlus
publish: true
---
C++における、[[コンテナ（C++）]]から要素を削除するためのプログラミングパターン。

[[algorithmヘッダ]]で提供されるstd::remove(先端イテレータ, 終端イテレータ, 除外したい値)` と `std::remove_if(先端イテレータ, 終端イテレータ, 除外条件)` は、指定したイテレータ範囲 `[begin, end)` から、除外対象の要素を後ろへ寄せ（寄せたとき、その値は保証されない）、除外対象ではない要素を前に詰めて[[コンテナ（C++）]]を変更し、この有効な要素列部分の終端の次を指すイテレータを返す。 
このイテレータを利用することで、`erase` と組み合わせて末尾に寄せられた不要部分をまとめて実際に削除できる。

一部の[[コンテナ（C++）]]￼では、イテレータの途中で要素を削除すると、それ以降にイテレータで参照したい要素のイテレータが無効化されてしまう（[[イテレータの無効化]]）ため、削除したい要素を末尾に回すことで、参照したい全ての要素の操作が終えた状態で、イテレータを安全に削除することができるため、これを実装する手段として利用できる。

例:
```cpp
#include <algorithm>
#include <iostream>
#include <vector>

// 配列表示用関数
template <typename T>
void print_vector(const std::vector<T> &v)
{
    for (auto &item : v)
    {
        std::cout << item << std::endl;
    }
}

int main()
{
    std::vector<int> v{1, 2, 3, 4, 5, 6};

    auto new_end = std::remove_if(v.begin(), v.end(), [](const auto &e)
                                  { return (e % 2) == 0; });
    print_vector(v);
    std::cout << "--After erase():--\n";

    v.erase(new_end, v.end());
    print_vector(v);
    return 0;
}

/* 実行結果:
1
3
5
4
5
6
---
1
3
5
*/
```

## References

- https://ja.wikibooks.org/wiki/More_C%2B%2B_Idioms/%E6%B6%88%E5%8E%BB%E3%83%BB%E5%89%8A%E9%99%A4(Erase-Remove)
- https://cpprefjp.github.io/reference/algorithm/remove_if.html
- https://cpprefjp.github.io/reference/vector/vector/erase.html
