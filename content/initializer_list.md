---
publish: true
tags:
  - CPlusPlus
---
`std::initializer_list`は`<initializer_list>`ヘッダで提供される。

[[リスト初期化]]で与えた値の並びを受け取るための標準ライブラリ型。  
コンパイラは`{ 1, 2, 3 }`のような初期化子リストを見ると、それを`std::initializer_list<T>`として扱えるようにする。

たとえば、クラスが`std::initializer_list<int>`を受け取る[[コンストラクタ（C++）]]を持っていれば、次のように初期化できる。

```cpp
IntArray array{ 5, 4, 3, 2, 1 };
```

```cpp
class IntArray
{
public:
    IntArray(std::initializer_list<int> list);
};
```

`std::initializer_list`は、要素そのものを所有しない軽量なビュー的型である。
要素は読み取り専用であり、`std::initializer_list`経由で書き換えることはできない。
`size()`で要素数を取得でき、`begin()`と`end()`で要素にアクセスできる。  
そのため、値渡しで受け取ることが多い。

## 用途

- 自作クラスを[[リスト初期化]]で初期化できるようにするとき
- 複数の値をまとめて受け取る関数や[[代入演算子（C++）]]を定義するとき

## 注意

非空の[[リスト初期化]]では、`std::initializer_list`を受け取るコンストラクタが、他の候補より優先される。

```cpp
IntArray a1(5);   // IntArray(int)
IntArray a2{ 5 }; // IntArray(std::initializer_list<int>)
```

そのため、`std::initializer_list`を受け取るコンストラクタを既存クラスに追加すると、波括弧初期化の意味が変わることがある。

## `=` による代入との関係

`array = { 1, 2, 3 };` のような代入を書くと、`std::initializer_list`を直接受け取る[[代入演算子（C++）]]が呼ばれるとは限らない。
そのような代入演算子が存在しない場合、コンパイラは初期化子リストから一時オブジェクトを作成し、それに対してコピー代入演算子やムーブ代入演算子を呼び出そうとする。  
このとき、暗黙生成されたコピー代入演算子が浅いコピーを行う型では、ダングリングポインタや二重解放の原因になることがある。

```cpp
IntArray array{};
array = { 1, 3, 5 };
```

このようなコードでは、`{ 1, 3, 5 }`から一時的な`IntArray`が作られ、それに対してコピー代入が行われることがある。  
そのコピー代入が浅いコピーであれば、一時オブジェクトの破棄後に`array`がダングリングポインタを持つ可能性がある。

そのため、`std::initializer_list`を受け取るコンストラクタを実装する型では、必要に応じて次のいずれかを検討する。

- `std::initializer_list`を受け取る[[代入演算子（C++）]]を実装する
- 適切なコピー代入演算子を実装する
- コピー代入演算子を削除する

## 関連

- [[リスト初期化]]

## 参考

- https://www.learncpp.com/cpp-tutorial/stdinitializer_list/
