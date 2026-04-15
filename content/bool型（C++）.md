---
publish: true
tags:
  - CPlusPlus
---
真偽値を表す[[基本型（C++）]]。
条件分岐によく用いられる。

整数との相互変換もできる。
`bool` から整数へ変換すると `false` は `0`、`true` は `1` になる。
整数から `bool` へ変換すると、`0` は `false`、それ以外は `true` になる。

[[標準ストリーム（C++）]]では、既定では `0` / `1` で出力される。
`true` / `false` で出力・入力したい場合は、`std::boolalpha` を使う。（オフにするなら `std::noboolalpha`）
