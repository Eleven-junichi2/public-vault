---
publish: true
tags:
  - CPlusPlus
---
`dynamic_cast`は型変換を実行時に検査しながら行う演算子。

主に[[仮想関数]]を持つ継承階層で、基底クラスへの[[ポインタ（C++）]]や[[左辺値参照（C++）]]を安全に派生クラスへ変換したいときに使う。

## 例

```cpp
class Base
{
public:
    virtual ~Base() = default;
};

class Derived : public Base
{
};

Base* b{ new Derived{} };
Derived* d{ dynamic_cast<Derived*>(b) };
```

この場合、`b`が実際に`Derived`を指していれば、`d`はそのアドレスを受け取る。

## 失敗時

ポインタへの`dynamic_cast`が失敗した場合、結果は`nullptr`になる。

```cpp
Base base{};
Base* b{ &base };
Derived* d{ dynamic_cast<Derived*>(b) }; // dはnullptr
```

参照への`dynamic_cast`が失敗した場合は、`std::bad_cast`例外が送出される。

## 関連

- [[ダウンキャスト]]
- [[アップキャスト]]

## 参考

- https://www.learncpp.com/cpp-tutorial/dynamic-casting/
