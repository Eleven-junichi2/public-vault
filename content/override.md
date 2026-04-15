---
publish: true
tags:
  - CPlusPlus
---
`override`は[[仮想関数]]を[[オーバーライド]]していることを明示する指定子。
新しい機能を与えるものではなく、その関数が本当に基底クラスの仮想関数をオーバーライドしているかをコンパイラに検査させるためのもの。

たとえば、`const`を付け忘れるなどしてシグネチャが一致しない場合、`override`があればコンパイルエラーになる。

```cpp
class Base
{
public:
    virtual void print() const
    {
    }
};

class Derived : public Base
{
public:
    void print() override
    {
    }
};
```

この例では、`Base::print() const`を正しくオーバーライドしていないためエラーになる。

## 例

```cpp
class Base
{
public:
    virtual void print() const
    {
    }
};

class Derived : public Base
{
public:
    void print() const override
    {
    }
};
```

## 参考

- https://www.learncpp.com/cpp-tutorial/the-override-and-final-specifiers-and-covariant-return-types/
