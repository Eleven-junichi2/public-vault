---
publish: true
tags:
  - CPlusPlus
---
constructor。
[[クラス型（C++）]]のオブジェクトを初期化するための特殊な[[メンバ関数]]。

コンストラクタはクラス名と同じ名前を持ち、返り値型を持たない。

```cpp
class Battery
{
public:
    Battery(float energy);
};
```

## 役割

クラス型のオブジェクトが作られるとき、コンストラクタはそのオブジェクトの初期状態を整えるために使われる。

```cpp
Battery pack { 0.9f };
```

呼び出し側が与えた初期値に合うアクセス可能なコンストラクタが見つからなければ、コンパイルエラーになる。

なお、[[集成体]]はコンストラクタを使わず、[[集成体#集成体初期化|集成体初期化]]で初期化されることがある。

## 定義

### クラス内で定義する

```cpp
class Battery
{
public:
    Battery(float energy)
    {
    }
};
```

### 宣言と定義を分ける

```cpp
class Battery
{
public:
    Battery(float energy); // 宣言
};

Battery::Battery(float energy) // 定義
{
}
```

## メンバ初期化子リスト

member initializer list。
コンストラクタ定義で、引数リストの後に `:` を書いてメンバの初期値を指定する。

```cpp
class Foo
{
private:
    int x_;
    int y_;

public:
    Foo(int x, int y)
        : x_ { x }, y_ { y } // member initializer list
    {
    }
};
```

メンバ初期化子リストを使うと、メンバは最初からその値で初期化される。

### 初期化順序

メンバは、メンバ初期化子リストに書いた順番ではなく、クラス内での**宣言順**で初期化される。

### デフォルトメンバ初期化子との関係

各メンバについて、初期値は次の優先順で決まる。

1. メンバ初期化子リストに指定があればそれを使う
2. そうでなければ、[[デフォルトメンバ初期化子]]があればそれを使う
3. そうでなければ、そのメンバは[[デフォルト初期化]]される

## 委譲コンストラクタ

あるコンストラクタから、同じクラスの別のコンストラクタへ初期化を委ねることができる。
これを委譲コンストラクタという。

```cpp
class Foo
{
private:
    int x_ {};
    int y_ {};

public:
    Foo(int x, int y)
        : x_ { x }, y_ { y }
    {
    }

    Foo()
        : Foo { 0, 0 }
    {
    }
};
```

この例では、引数なしコンストラクタが `Foo(int, int)` に処理を委譲している。

## コンパイラ生成コンストラクタ

コンストラクタを自分で宣言しない場合、コンパイラが自動生成することがある。

- [[デフォルトコンストラクタ（C++）]]
- [[コピーコンストラクタ（C++）]]
- [[ムーブコンストラクタ]]

## 補足

- コンストラクタは通常の関数のように名前で直接呼び出すものではなく、オブジェクト初期化の一部として使われる
- メンバの初期化には、代入よりメンバ初期化子リストのほうが自然なことが多い
- `const` メンバや参照メンバは、メンバ初期化子リストで初期化する必要がある

## 関連

- [[メンバ関数]]
- [[デフォルトコンストラクタ（C++）]]
- [[コピーコンストラクタ（C++）]]
- [[集成体]]

## 参考

- https://www.learncpp.com/cpp-tutorial/default-constructors-and-default-arguments/
- https://www.learncpp.com/cpp-tutorial/constructor-member-initializer-lists/
- https://www.learncpp.com/cpp-tutorial/delegating-constructors/
