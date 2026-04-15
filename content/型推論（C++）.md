---
publish: true
tags:
  - CPlusPlus
---
type deduction。type inference。

型を明示しない一部の文脈で、コンパイラが型を決定する仕組み。
変数定義では `auto` キーワードを用いて利用できる。

```cpp
auto d { 5.0 }; // 5.0 は double リテラルなので、d は double と推論される
```


## 文字列リテラルの型推論

`std::string`または`std::string_view`に推論されたい場合、それらの[[文字列（C++）#リテラル]]を利用する。

```cpp
using namespace std::literals;
auto s1 { "weeee"s } // "weeee"sはstd::stringのリテラル
```


## 返り値の型推論

関数の返り値の型として `auto` キーワードを使用できる。
この場合、return文から型を決定する。
なお、コンパイル時に型を決定するため、複数のreturn文がそれぞれ異なる型を返す可能性がある場合エラーとなる。

前方宣言を利用している場合に、戻り値の型が変更されても、関数定義の修正のみで済むメリットがあるが、前方宣言で返り値の型がわからないので可読性は低下する。

通常の関数宣言では、関数パラメータの型を単に `auto` で省略することはできない。
ただし、C++20 以降では abbreviated function templates のように、`auto` を用いる文脈もある。

## 関連する構文

`auto`キーワードによって、返り値の型を後置する構文を利用できる。
返り値の型について、関数パラメータの変数を利用して表現することができる。
単に可読性を上げるためにも利用される。

```cpp
// パラメータの変数aとbを+演算子で足し合わせた結果の型を、
// 関数g()の戻り値型とする
auto g(int a, int b) -> decltype(a + b)
{
  return a + b;
}
```

## 参考

- https://cpprefjp.github.io/lang/cpp11/trailing_return_types.html
- https://www.learncpp.com/cpp-tutorial/type-deduction-for-functions/
