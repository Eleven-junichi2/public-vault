---
publish: true
tags:
  - CPlusPlus
---
`decltype(式)`によって、名前や式から[[型（C++）]]を得ることができる。
ただし、結果は式の値カテゴリの影響を受け、`T`、`T&`、`T&&`のいずれかになることがある。

例えば、`x`が`int`型の変数なら、`decltype(x)`は`int`だが、`decltype((x))`は`int&`になる。
これは、`x`は名前そのものとして扱われるのに対し、`(x)`は括弧で囲まれた式として扱われるためである。
`decltype`では、この違いが結果の型に影響する。

用途:

- 式や名前から型を取り出す
- 関数の戻り値型を表現する
- 関連型を取り出す

```cpp
int x{ 0 };
decltype(x) a{ 1 };   // int
decltype((x)) b{ x }; // int&
```

```cpp
auto g(int a, int b) -> decltype(a + b)
{
    return a + b;
}
```

```cpp
decltype(arr)::size_type i{ 0 };
```

## 参考

- https://eel.is/c++draft/dcl.type.decltype
- https://en.cppreference.com/w/cpp/language/decltype
