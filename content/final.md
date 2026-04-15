---
publish: true
tags:
  - CPlusPlus
---
final。

それ以上の[[継承（C++）|継承]]や[[オーバーライド]]を禁止する指定子。

## 関数に付ける場合

`final`を付けると、その関数はそれ以上の派生クラスでオーバーライドできなくなる。

```cpp
class Base
{
public:
    void print() const final
    {
    }
};
```

この場合、`Base`を継承したクラスで`print()`をオーバーライドしようとするとコンパイルエラーになる。

## クラスに付ける場合

クラス名に`final`を付けると、そのクラスは基底クラスとして使えなくなる。

```cpp
class A final
{
};
```

この場合、`A`を継承することはできない。

## 用途

- これ以上の派生で振る舞いを変更させたくないとき
- クラス設計上、そのクラスを継承させたくないとき

## 参考

- https://www.learncpp.com/cpp-tutorial/the-override-and-final-specifiers-and-covariant-return-types/
