---
publish: true
tags:
  - CPlusPlus
---
`noexcept`指定子。

関数が、**呼び出し元から見える**例外を送出しないことを表すための指定子。
関数の中で例外を投げること自体を文法上禁止するものではない。
ただし、それらの例外が関数の外へ出てはいけない。

## 概要

C++では関数は、

- 例外を外へ送出しない関数
- 例外を外へ送出する可能性がある関数

のどちらかとして扱われる。

関数を例外を外へ送出しない関数として宣言するには、関数宣言の引数リストの右側に`noexcept`を付ける。

```cpp
void doSomething() noexcept;
```

これは`noexcept(true)`と同じ意味である。  
一方、`noexcept(false)`は、その関数が例外を送出する可能性があることを表す。

## `noexcept`違反

`noexcept`関数から未処理の例外が外へ出ようとすると、`std::terminate`が呼ばれる。

```cpp
void f() noexcept
{
    throw 1; // 外へ出るとstd::terminate
}
```

この場合、上位に対応する`catch`が存在していても、その前に`std::terminate`される。

また、`std::terminate`時にはstack unwinding（スタック巻き戻し）が行われるかどうかが実装依存になることがある。

## `noexcept`とオーバーロード

例外指定だけが異なる関数を[[オーバーロード]]することはできない。

```cpp
void f();
void f() noexcept; // エラー
```

## `noexcept`演算子

`noexcept`は演算子としても使える。  
この場合、式が例外を送出する可能性がないとコンパイラが判断すれば`true`、そうでなければ`false`になる。

```cpp
void foo() { throw -1; }
void goo() noexcept {}

constexpr bool b1{ noexcept(5 + 3) }; // true
constexpr bool b2{ noexcept(foo()) }; // false
constexpr bool b3{ noexcept(goo()) }; // true
```

`noexcept`演算子は式を実行しない。  
コンパイル時に、その式が例外を送出しうるかどうかを調べる。

## どんな関数に付けるか

`noexcept`は、単に「今の実装ではたまたま例外を投げていない」関数に付けるものではない。  
その関数が、設計上も例外を外へ出さないことを保証したい場合に付ける。

特に`noexcept`が重要なのは、

- [[ムーブコンストラクタ]]
- [[ムーブ代入演算子（C++）]]
- `swap`関数

である。

これらが`noexcept`であると、標準ライブラリがより効率のよい実装を選べることがある。

また、[[デストラクタ（C++）]]のように、例外を外へ出してはいけない関数でも重要である。

## 古い例外指定

かつては

```cpp
void f() throw();
void g() throw(std::out_of_range);
```

のような動的例外指定が使われていたが、これは非推奨となり、その後のC++で削除された。  
現在は`noexcept`を使う。

## 関連

- [[例外処理（C++）]]
- [[std::terminate]]
- [[ムーブコンストラクタ]]
- [[ムーブ代入演算子（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/exception-specifications-and-noexcept/
- https://cpprefjp.github.io/lang/cpp11/noexcept.html
