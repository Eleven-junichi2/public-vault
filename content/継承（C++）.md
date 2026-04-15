---
publish: true
tags:
  - CPlusPlus
---
inheritance。

[[クラス（C++）]]どうしの関係の一種で、あるクラスが別のクラスのメンバを受け継ぐ仕組み。  
[[コンポジション]]が`has-a`関係を表すのに対し、継承は`is-a`関係を表す。

継承元のクラスを基底クラス（parent class/base class/superclass）、継承先のクラスを派生クラス（child class/derived class/subclass）という。

派生クラスは、基底クラスのメンバ変数とメンバ関数を受け継ぎ、さらに自分固有のメンバを追加できる。

派生クラスの[[オブジェクト（C++）]]を構築するときは、最も上位の基底クラスから順に構築され、最後に最も下位の派生クラスが構築される。

たとえば`A <- B <- C`という継承関係で`C`のオブジェクトを作ると、構築順は`A → B → C`になる。

## 基本構文

```cpp
class Derived : public Base
{
};
```

`class Derived : public Base`の部分で、`Derived`が`Base`を公開継承していることを表す。

## 基底クラスのコンストラクタ呼び出し

派生クラスの[[コンストラクタ（C++）]]は、自分自身のメンバだけでなく、どの基底クラスのコンストラクタを呼ぶかも決める。  
派生クラスの[[メンバー初期化リスト]]で基底クラス名を書くと、そのコンストラクタを明示的に呼び出せる。

```cpp
class Base
{
public:
    Base(int id)
    {
    }
};

class Derived : public Base
{
public:
    Derived(int id, double cost)
        : Base{ id }
    {
    }
};
```

基底クラスのコンストラクタを指定しない場合は、**基底クラスのデフォルトコンストラクタを自動的に呼び出す**。  
そのため、基底クラスにデフォルトコンストラクタが無いなら、どの基底クラスコンストラクタを使うかを明示する必要がある。

なお、派生クラスは基底クラスから継承したメンバ変数を、自分のメンバー初期化リストで直接初期化することはできない。  
基底クラス部分の初期化は、基底クラスのコンストラクタが担当する。

## 例

```cpp
#include <string>
#include <string_view>

class Person
{
public:
    std::string m_name{};
    int m_age{};

    Person(std::string_view name = "", int age = 0)
        : m_name{ name }, m_age{ age }
    {
    }

    const std::string& getName() const { return m_name; }
    int getAge() const { return m_age; }
};

class BaseballPlayer : public Person
{
private:
    double m_battingAverage{};
    int m_homeRuns{};

public:
    BaseballPlayer(std::string_view name = "", int age = 0,
        double battingAverage = 0.0, int homeRuns = 0)
        : Person{ name, age }
        , m_battingAverage{ battingAverage }
        , m_homeRuns{ homeRuns }
    {
    }

    double getBattingAverage() const { return m_battingAverage; }
    int getHomeRuns() const { return m_homeRuns; }
};
```

この例では、`BaseballPlayer`は`Person`を継承している。  
`BaseballPlayer`のコンストラクタは、`Person{ name, age }`によって基底クラス`Person`のコンストラクタを呼び出し、`m_name`と`m_age`を初期化している。  
そのうえで、自分のメンバである`m_battingAverage`と`m_homeRuns`を初期化する。

`BaseballPlayer`は`Person`である、と言えるので、継承を使うのが自然である。

## 破棄順

破棄は構築と逆順で行われる。  
つまり、派生クラスの[[デストラクタ（C++）]]が先に呼ばれ、その後で基底クラスのデストラクタが呼ばれる。

## 継承の利点

- 基底クラスのメンバを再定義せずに再利用できる
- 共通部分を基底クラスにまとめられる
- 基底クラスを変更すると、その変更が派生クラスにも反映される

## 注意

継承は`is-a`関係を表すときに使う。  
単に別のオブジェクトをメンバとして持つだけなら、[[コンポジション]]や[[集約]]のほうが適切な場合がある。

## 参考

- https://www.learncpp.com/cpp-tutorial/basic-inheritance-in-c/
- https://www.learncpp.com/cpp-tutorial/order-of-construction-of-derived-classes/
- https://www.learncpp.com/cpp-tutorial/constructors-and-initialization-of-derived-classes/
