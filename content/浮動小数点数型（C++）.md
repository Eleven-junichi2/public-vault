---
publish: true
tags:
  - CPlusPlus
---
[[浮動小数点数]]を有限精度で近似的に表現する型。

## float

単精度の浮動小数点数型。

## double

倍精度の浮動小数点数型。

## long double

`double` 以上の精度を持つ浮動小数点数型。

サイズや精度は処理系に依存するが、多くの環境では `float` は4バイト、`double` は8バイトである。

## リテラル

浮動小数点リテラルは、接尾辞がなければ `double` である。
`f` を付けると `float`、`L` を付けると `long double` になる。
例: `5.0f` は `float`、`5.0` は `double`、`5.0L` は `long double`

## 参考

- https://www.learncpp.com/cpp-tutorial/floating-point-numbers/
