---
publish: true
tags:
  - CPlusPlus
---
`std::array`。
`<array>`ヘッダで提供される、固定長の配列を表現する[[コンテナ（C++）]]の[[クラステンプレート]]。
[[配列（C言語）]]と同様に要素は連続して配置され、長さの情報も保持する。
要素型が対応していれば、コピーや[[ムーブセマンティクス|ムーブ]]も行える。
そのため、[[配列（C言語）]]より値として扱いやすい。

宣言の例:
```cpp
#include <array>

int main()
{
    std::array<int, 5> a {}; // int型で長さ5のarrayの変数`a`
}
```
- 長さには、テンプレート引数として[[コンパイル時定数]]が必要
- 初期化子があれば、型と長さは[[クラステンプレート引数推論]]で省略できる。
- 配列を[[constexpr]]と[[const（C++）]]として宣言できる。

## 集成体初期化

`std::array`は[[集成体]]であり、[[集成体#集成体初期化|集成体初期化]]を行える。

## 長さと添字の型

`std::array<T, N>` の `N` は型の一部であり、`std::array<int, 3>` と `std::array<int, 4>` は別の型になる。
長さや添字を表す型として `size_type` を持つ。
多くの場合は `std::size_t` に近い型である。

## 長さを取得する

### 符号なし整数として

`size_type`型で長さを返す`size()`メンバ関数を利用する。

### 符号付き整数として

C++20 では、普通 `std::ptrdiff_t` 型で長さを返す `std::ssize()` 関数を利用できる。

## 長さが0の std::array

長さが0の`std::array`の要素へのアクセスは未定義動作を起こす。
長さが0であるかは`empty()`メンバ関数の真偽値で確かめられる。

## 要素に添字でアクセスする

- [[添字演算子（C++）]]
- `at(添字)`メンバ関数
- `std::get<添字>()`

### 各方法の違い

- `at()` は添字が配列の範囲外であるかを実行時に境界チェックする（例外を投げる）
- `std::get<添字>()` は添字をテンプレート引数で指定し、範囲外ならコンパイルエラーになる

## 複合型のarray

`std::array`はある1つの[[配列（C言語）|C言語スタイルの配列]]メンバで要素を管理する構造体として定義されているため、本来であれば初期化の際、各要素を一つの[[リスト初期化]]の`{}`でまとめて渡す必要がある。しかし、各要素がスカラー値の場合は、この工程を省略できる（**brace elision**）[^brace_elision]。
[[複合型（C++）]]の要素を持つ場合は、初期化で入れ子の `{}` が必要になることがある。

例:
```cpp
constexpr std::array<House, 3> houses {
    {
        { 13, 4, 30 },
        { 14, 3, 10 },
        { 15, 3, 40 },
     }
};
```

## 参照を要素として持つ

[[array（C++）]]は要素を代入で可能な[[オブジェクト（C++）]]として持つ必要があるが、参照は[[オブジェクト（C++）]]ではないため、要素として持つことができない。
解決策として、`<functional>`ヘッダで提供される`std::reference_wrapper`[[クラステンプレート]]で、任意の型の変更可能な[[左辺値参照（C++）]]を包んで持つことができる。
`std::reference_wrapper<T>`は暗黙的に`T&`へ変換される。`get()`メンバ関数でも明示して`T&`を得られる。

```cpp
#include <array>
#include <functional> // for std::reference_wrapper
#include <iostream>

int main()
{
    int x { 1 };
    int y { 2 };
    int z { 3 };

    std::array<std::reference_wrapper<int>, 3> arr { x, y, z };

    arr[1].get() = 5; // modify the object in array element 1

    std::cout << arr[1] << y << '\n'; // show that we modified arr[1] and y, prints 55

    return 0;
}
```

## 多次元配列

テンプレート引数での、配列の要素の型指定に配列を指定してネストすることで実現する。

```cpp
std::array<std::array<型, 長さ>, 長さ> arr {{}}; // {}でもok
```

### エイリアステンプレートで扱いやすくする

多次元配列の[[エイリアステンプレート]]を用意することで、初期化や次元ごとの長さの取得などを簡潔化できる。

```cpp
template <typename T, std::size_t Row, std::size_t Col>
using Array2d = std::array<std::array<T, Col>, Row>;

template <typename T, std::size_t Row, std::size_t Col>
constexpr int rowLength(const Array2d<T, Row, Col>&) // `int`ではなく`std::size_t`を返すようにしても良い
{
    return Row;
}


```

## 参考

- https://www.learncpp.com/cpp-tutorial/introduction-to-stdarray/
- https://www.learncpp.com/cpp-tutorial/stdarray-of-class-types-and-brace-elision/
- https://www.learncpp.com/cpp-tutorial/multidimensional-stdarray/

[^brace_elision]: https://cpprefjp.github.io/lang/cpp14/brace_elision_in_array_temporary_initialization.html
