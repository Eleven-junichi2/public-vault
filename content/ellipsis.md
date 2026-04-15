---
publish: true
tags:
  - CPlusPlus
---
関数の引数リストの末尾に `...` を書いて、可変長引数を受け取る方法。

## `<cstdarg>` によるアクセス

`<cstdarg>` で提供される機能を使うと、可変長引数をたどれる。
`va_start` で引数をたどるには、最後の非 `...` 引数が必要になる。

- `va_list`
  可変長引数にアクセスするための型
- `va_start(list, 最後の非 ... 引数)`
  `va_list` を初期化するマクロ
- `va_arg(list, 型)`
  次の引数を取り出す
- `va_end(list)`
  後始末を行う

可変長引数は次の危険性があるため、あまり利用は推奨されない:
- コンパイラが型を検証できず、型の誤りに関する警告を出せない
- 引数の個数や型について、呼び出し側と受け取り側で別途規約を共有する必要がある

## 例

```cpp
#include <cstdarg>
#include <iostream>

double findAverage(int count, ...)
{
    int sum{ 0 };
    va_list list;
    va_start(list, count);

    for (int arg{ 0 }; arg < count; ++arg)
    {
         sum += va_arg(list, int);
    }

    va_end(list);
    return static_cast<double>(sum) / count;
}

int main()
{
    std::cout << findAverage(5, 1, 2, 3, 4, 5) << '\n';
    std::cout << findAverage(6, 1, 2, 3, 4, 5, 6) << '\n';
}
```

## 関連

- [[マクロ（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/ellipsis-and-why-to-avoid-them/
