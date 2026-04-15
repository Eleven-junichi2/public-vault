---
publish: true
tags:
  - CPlusPlus
---
`std::reference_wrapper`。`<functional>`ヘッダで提供される、参照をコピー可能・代入可能な形で保持するラッパー。

参照のようにオブジェクトを参照できるが、参照そのものと違ってコピーや代入ができる。  
そのため、`std::vector`のようなコンテナに「参照のようなもの」を格納したいときに使う。

たとえば、通常の参照は再束縛できないため、コンテナの要素型としてそのまま扱いにくい。

```cpp
std::vector<const Teacher&> teachers; // エラー
```

このような場合に、`std::reference_wrapper`を使う。

```cpp
std::vector<std::reference_wrapper<const Teacher>> teachers;
```

`std::reference_wrapper`から元のオブジェクトを取り出すには、`get()`メンバ関数を使う。
また、場面によっては `T&` として暗黙的に使える。

```cpp
for (auto teacher : teachers)
{
    std::cout << teacher.get().getName() << '\n';
}
```

## `std::ref`と`std::cref`

`std::reference_wrapper`オブジェクトを生成する補助関数。
`std::ref` は変更可能な参照を、`std::cref` は `const` 参照を包みたいときに使う。

```cpp
int x { 5 };
auto ref { std::ref(x) };   // std::reference_wrapper<int>
auto cref { std::cref(x) }; // std::reference_wrapper<const int>
```

## 用途

- [[集約]]で、外部に存在するオブジェクトへの参照を複数保持したいとき
- コンテナに参照そのものは入れられないため、その代わりとして使うとき

## 注意

- `std::reference_wrapper`は[[所有権]]を持たない
- 参照先オブジェクトの[[生存期間（C++）]]は自分で管理する必要がある
- 匿名オブジェクト（一時オブジェクト）を包むと、すぐにダングリング参照になるため使えない

## 参考

- https://www.learncpp.com/cpp-tutorial/aggregation/
