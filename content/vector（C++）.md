---
publish: true
tags:
  - CPlusPlus
---
`std::vector` は、`<vector>`ヘッダで提供される、配列を表現する[[コンテナ（C++）]]である[[クラステンプレート]]。
要素は連続して配置され、長さを実行時に変更できる。
[[ムーブセマンティクス]]に対応している。

## 例

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector primes { 2, 3, 5, 7, 11 };

    std::cout << "The first prime number is: " << primes[0] << '\n';
    std::cout << "The second prime number is: " << primes[1] << '\n';
    std::cout << "The sum of the first 5 primes is: " << primes[0] + primes[1] + primes[2] + primes[3] + primes[4] << '\n';

    return 0;
}
```

## 要素数を指定する初期化

要素数を明示的に指定できるコンストラクタとして`explicit std::vector<T>(std::size_t)`が定義されているため、これを利用する。これは各要素について[[ゼロ初期化]]する。

```cpp
std::vector<int> data(10);
```

## const

`std::vector`は[[const（C++）]]で修飾できる。このとき`vector`は必ず初期化される必要があり、変更不可能になる（要素も`const`として扱われる。）

```cpp
#include <vector>

int main()
{
    const std::vector<int> prime { 2, 3, 5, 7, 11 }; // std::vector<const int>はできない

    return 0;
}
```

## constexpr

C++20以降では`std::vector`のメンバ関数の多くは[[constexpr]]として使える。
ただし、`std::vector`は動的メモリ確保を行うため、一般に`constexpr`オブジェクトとして長く保持する用途には向かない。
固定長の[[constexpr]]配列を扱いたい場合は、`std::array`のほうが向いている。

## at()

配列へのインデックスによるアクセスについて、[[添字演算子（C++）]]では境界外へのアクセスが[[未定義動作]]となるが、`at()`メンバ関数によるアクセスでは、実行時の境界チェックを行い、範囲外なら例外を投げる。

## capacity

容量。メモリが既に確保された(メモリを再確保せずに格納できる)最大の要素数。
`capacity()`メンバ関数で取得できる。

## size

要素数（長さ）は`size()`メンバ関数で取得できる。

## リサイズ

`resize()`で、配列の長さを変更する。
以前より長くする場合は、新しい要素が追加される。新しい長さが配列が確保するメモリの容量を超える場合、[[#メモリの再割り当て]]が行われる。
以前より配列を小さくする場合は、要素数だけ減らし、すでに確保したメモリの容量は変更しない。

## メモリの再割り当て

容量が不足した状態で要素を追加するなど、より大きな記憶領域が必要になると、再割り当て（reallocation）が行われる。
- 必要な要素数を収められる新しいメモリ領域を確保する
- 既存の要素を新しいメモリ領域へコピーまたは[[ムーブセマンティクス|移動]]する
- 以前のメモリ領域を解放する

再割り当ては配列全体を新しい場所へ移す操作になるので、高価な操作になりやすい。
また、再割り当てが起こると、要素へのポインタ・参照・イテレータは無効化されうる。

## 容量の縮小

`shrink_to_fit()`で配列が確保するメモリの容量を配列の長さに近づけるよう要求できる。
ただし、これは非拘束の要求であり、実際に容量が縮小されるとは限らない。

## スタック操作

配列をスタックのように操作する[^vector_as_stack]メンバ関数が用意されている。
スタックとして使う場合は、配列の末尾をスタックの先頭としてみなす。
- `push_back()`: 新しい要素を配列の末尾に追加する（コピーまたはムーブ）
- `pop_back()`: 配列の末尾の要素を削除する
- `back()`: 配列の末尾の要素を取得する
- `emplace_back()`: `push_back()`の代替版。
	- `push_back()`との違い: 引数から末尾で直接オブジェクト構築する。状況によっては一時オブジェクトの生成やコピー・ムーブを省ける。
新しい要素を追加する操作は、配列の長さを増やすため、配列の容量が不足すると[[#メモリの再割り当て]]を起こす。この時、効率性のために、コンパイラ次第で新しい要素分以上に余分を持って容量を変更する。

## 長さを変えずに容量を変更する

`reserve()`を使う。
これは要素数を変えずに、必要な容量を先に確保して再割り当て回数を減らしたいときに使う。

長さを設定せずに容量だけ設定して初期化する例：
```cpp
std::vector<int> stack{}; // 空なので要素なし（つまり長さ0）
stack.reserve(6); // 容量6
```

## std::vector\<bool>

`std::vector<bool>` は、`bool` 型に対して特別に定義された `std::vector` の[[クラステンプレートの特殊化|特殊化]]である。
メモリ使用量を抑えるために最適化されているが、その代償として通常の `std::vector<T>` と性質が少し異なる。

### 1. 空間最適化の仕組み（Bit-packing）

通常の `std::vector<T>` は各要素を個別のオブジェクトとして保持するが、`std::vector<bool>` は典型的には**ビットパッキング**を用いて複数の値をまとめて格納する。

- **メモリ節約**: `bool` 値をビット単位で表現することで、通常の `std::vector<bool>` 以外のコンテナより少ないメモリで保持しやすい。
- **効率**: メモリ使用量の面では有利になりやすいが、アクセスや更新は単純な `bool` 配列より複雑になる。

### 2. プロキシオブジェクト（Proxy Objects）による制約

C++ の仕様上、個々のビットに対して直接 `bool&` を作ることはできない。
そのため、`std::vector<bool>` は参照の代わりに**プロキシオブジェクト**を返す。

- **戻り値の型**: `operator[]` や `at()` は、`bool&` ではなく `std::vector<bool>::reference` という特殊な型を返す。
- **性質**: この型は `bool` 参照のように使えるよう設計されているが、通常の `bool&` と同一ではない。

### 3. 発生しやすい問題とバグの種

`v[0]` は `bool&` ではなく特殊な参照型を返すため、通常の参照を前提にしたコードが壊れやすい。

```cpp
std::vector<bool> v { true };
// auto& ref = v[0]; // コンパイルエラー
```

- **参照の扱いが特殊**: `auto&` や `T&` を前提にした汎用コードと相性が悪い。
- **性能面の注意**: ビット単位での読み書きには追加の処理が必要になるため、メモリ節約が不要な場面では逆に遅くなることがある。
- **アドレスを取りにくい**: 要素を通常の `bool` オブジェクトとして保持していないため、`bool*` を期待するコードとは噛み合わない。

### 4. 推奨される代替案

特別なメモリ制約がない限り、以下の代替案のほうが扱いやすいことが多い。

| 代替手段              | 特徴                                   |
| ----------------- | ------------------------------------ |
| std::deque<bool>  | 連続メモリではないが、`std::vector<bool>` 特有のビット圧縮を避けたいときの候補。 |
| std::vector<char> | bool の代わりに char を使うことで、直感的かつ高速に動作する。 |
| std::bitset       | 要素数がコンパイル時に固定されている場合に最適。             |

## 参考

- https://learn.microsoft.com/ja-jp/cpp/cpp/arrays-cpp?view=msvc-170
- https://www.learncpp.com/cpp-tutorial/introduction-to-containers-and-arrays/
- https://www.learncpp.com/cpp-tutorial/introduction-to-stdvector-and-list-constructors/
- https://cpprefjp.github.io/reference/vector/vector.html

[^vector_as_stack]: https://www.learncpp.com/cpp-tutorial/stdvector-and-stack-behavior/
