---
publish: true
tags:
  - CPlusPlus
---
派生クラスを定義するときに、基底クラスを`public` / [[protected]] / `private`のどれで[[継承（C++）|継承]]するかを指定するもの。

この指定は、基底クラスのメンバが派生クラス側でどの[[アクセスレベル]]として扱われるかに影響する。

## 基本構文

```cpp
class Derived : public Base
{
};
```

`public`の部分が、継承に対する[[アクセス指定子]]である。

## 変化のしかた

基底クラスのメンバは、継承方法によって派生クラス側で次のように扱われる。

| 基底クラスでのアクセス | `public`継承 | `protected`継承 | `private`継承 |
| --- | --- | --- | --- |
| `public` | `public` | `protected` | `private` |
| `protected` | `protected` | `protected` | `private` |
| `private` | アクセス不可 | アクセス不可 | アクセス不可 |

基底クラスの`private`メンバは、どの継承方法でも派生クラスから直接アクセスできない。

## public継承

基底クラスの`public`メンバは派生クラスでも`public`のままで、`protected`メンバも`protected`のままである。

```cpp
class Base
{
public:
    int m_public{};

protected:
    int m_protected{};
};

class Derived : public Base
{
public:
    void f()
    {
        m_public = 1;
        m_protected = 2;
    }
};
```

`public`継承は`is-a`関係を表すときに使う最も一般的な継承方法である。

## protected継承

基底クラスの`public`メンバと`protected`メンバは、どちらも派生クラスでは`protected`として扱われる。

外部には公開したくないが、さらにその派生クラスからは使えるようにしたい場合に使われることがある。  
ただし、実際にはあまり使われない。

## private継承

基底クラスの`public`メンバと`protected`メンバは、どちらも派生クラスでは`private`として扱われる。

```cpp
class Base
{
public:
    int m_public{};

protected:
    int m_protected{};
};

class Derived : private Base
{
public:
    void f()
    {
        m_public = 1;
        m_protected = 2;
    }
};
```

この場合、`Derived`のメンバ関数からはアクセスできるが、`Derived`の外部からは基底クラス由来のメンバへアクセスできない。

`private`継承は、`is-a`関係というより、基底クラスを内部実装として利用したい場合に使われることがある。  
ただし、これも実際にはあまり使われない。

## 注意

- 継承方法を省略すると、[[クラス（C++）]]では`private`継承になり、[[構造体（C++）]]では`public`継承になる。
- これらの規則は、メンバ変数だけでなく[[メンバ関数]]やクラス内で宣言された型にも当てはまる
- 一般には、特別な理由がない限り`public`継承を使う
- 基底クラスのメンバは、可能なら`protected`より`private`を優先する

## 参考

- https://rinatz.github.io/cpp-book/ch07-03-inheritance/
- https://www.learncpp.com/cpp-tutorial/inheritance-and-access-specifiers/
