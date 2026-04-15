---
publish: true
tags:
  - CPlusPlus
---
`assert`。
`<cassert>` で提供されるマクロ。
[[マクロ（C++）]]の一種で、関数のような書き方をする。

評価した式が `false` のとき、診断してプログラムを停止する。
主にデバッグ時の実行時チェックに使う。

## 説明を付与する

[[文字列リテラル（C++）]] が `true` に評価されることを利用し、[[論理演算子（C++）]] の `&&` を用いてメッセージを付けることがある。

```cpp
assert(someCondition && "This is error msg");
```

## NDEBUG

`NDEBUG` マクロを定義すると、`assert` は無効になる。

## 関連

- [[アサーション]]
- [[static_assert]]
- [[マクロ（C++）]]

## 参考

- https://learn.microsoft.com/ja-jp/visualstudio/debugger/c-cpp-assertions?view=visualstudio
