---
publish: true
tags:
  - CPlusPlus
---
既存の[[型（C++）]]に別名を付ける仕組み。
可読性の向上や、プラットフォーム差異の吸収などのために用いられる。

## using

C++ では、主に `using` を用いて型エイリアスを定義する。

例：
```cpp
using Distance = double;

Distance milesToDestination{ 3.4 }; // double型の変数
```

[[エイリアステンプレート]]も `using` を用いて定義する。

## エイリアスの命名

命名規則はプロジェクトごとに異なる。
慣習的に `_t` を付ける流儀もあるが、POSIX ではグローバルスコープの `_t` 名が予約されているため、ユーザーコードでは避けることがある。

## 型エイリアスのスコープ

型名として導入された名前も、[[スコープ（C++）]]や[[宣言領域（C++）]]の影響を受ける。

## typedef

型エイリアスを作成する古い方法。
`typedef 型 エイリアスの名前`
現在でも使えるが、可読性やテンプレートとの相性の面から、新しいコードでは `using` が好まれることが多い。

## 参考

- https://learn.microsoft.com/ja-jp/cpp/cpp/aliases-and-typedefs-cpp?view=msvc-170
- https://www.learncpp.com/cpp-tutorial/typedefs-and-type-aliases/
