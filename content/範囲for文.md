---
publish: true
tags:
  - CPlusPlus
---
range-based for statement(for-each loop)。
配列やコンテナの全要素を順に処理するための[[for文]]。
C++11 で導入された。

## 基本形式
```cpp
for (要素宣言 : 範囲式) {
    // ループ本体
}
```

## 初期化文付き形式
```cpp
for (初期化文; 要素宣言 : 範囲式) {
    // インデックス変数などを併用可能
}
```

添字を自分で管理しなくてよいため、全要素に対する処理を書きやすい。

## 要素宣言の例

- `const auto&`
  読み取るだけの場合。
- `auto&`
  元の要素を書き換える場合。
- `auto`
  コピーして扱う場合。

## 補足

- 逆順走査や添字が必要な場合は、通常の[[for文]]やイテレータを使うことがある。
- C++20 以降では、初期化文付きの範囲for文も使える。

## 参考

- https://cpprefjp.github.io/lang/cpp11/range_based_for.html
- https://www.learncpp.com/cpp-tutorial/range-based-for-loops-for-each/
