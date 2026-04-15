---
publish: true
tags:
  - CPlusPlus
---
`static_assert`。
コンパイル時に条件を検証するための文。
[[assert]] と違ってマクロではなく、C++ のキーワードである（キーワードなので、ヘッダのインクルードは不要。）

`static_assert(条件式, 診断メッセージ)` の形で書く。
条件が成り立たなければ、コンパイルエラーになる。

実行時コストはなく、[[コンパイル時定数]]や[[constexpr]]に関わる条件の検証に使われる。


```cpp
static_assert(sizeof(int) >= 4, "int is too small");
```

## 関連

- [[アサーション]]
- [[assert]]
- [[コンパイル時評価]]

## 参考

- https://en.cppreference.com/w/cpp/language/static_assert
