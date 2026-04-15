---
publish: true
tags:
  - CPlusPlus
---
[[ストリーム（C++）]]に `<<` や `>>` で渡し、入出力の挙動や書式設定を変えるもの。

入力向けのものもあれば、出力向けのものもある。
また、`<iomanip>` は書式設定系のマニピュレータを多く提供するヘッダである。
これらの設定の多くは `std::ios` 系の状態としてストリーム内に保持される。
内部的には `setf()` / `unsetf()` のような低レベル API でも制御できるが、通常はマニピュレータの方が読みやすい。

## 永続する設定

次のようなマニピュレータは、設定後もしばらく有効なまま残る。

- `std::boolalpha` / `std::noboolalpha`
  `true` / `false` で出すか、`1` / `0` で出すか
- `std::hex` / `std::dec` / `std::oct`
  整数の基数
- `std::fixed` / `std::scientific`
  浮動小数点数の表記法
- `std::showpos` / `std::noshowpos`
  正の数にも `+` を付けるか
- `std::uppercase` / `std::nouppercase`
  16 進数や指数表記の英字を大文字にするか
- `std::showpoint` / `std::noshowpoint`
  必要最小限でなくても小数点以下を表示するか
- `std::left` / `std::right` / `std::internal`
  幅指定時の寄せ方

```cpp
std::cout << std::boolalpha << true << '\n';
std::cout << std::hex << 27 << '\n';
std::cout << std::showpos << 27 << '\n';
std::cout << std::uppercase << std::scientific << 123.0 << '\n';
```

これらはストリームの状態として残るため、必要なら `std::dec` や `std::noshowpos` などで戻す。

## その場で使う設定

次のようなマニピュレータは、主に直後の入出力を調整するために使う。

- `std::ws`
  入力時に先頭の空白文字を読み飛ばす
- `std::setw`
  次の出力の表示幅を設定する
- `std::setfill`
  幅が足りないときに埋める文字を設定する
- `std::endl`
  改行して[[フラッシュ]]する
- `std::flush`
  改行せずにフラッシュする
- `std::setprecision`
  浮動小数点数の精度を設定する

## std::endl

改行文字を出力し、出力バッファをフラッシュする。
単なる改行より動作が重くなることがあるため、改行だけで十分なら `'\n'` が使われることも多い。

## std::ws

入力時に、先頭の空白文字を読み飛ばす。
直前の入力で残った改行文字を読み飛ばしたいときなどに使う。

## std::hex

整数の入出力を 16 進数で行うように設定する。
これはストリームの状態を変更するため、その後の整数入出力にも影響する。

## std::setw

次の出力の表示幅を設定する。
`<iomanip>`ヘッダで提供され、主に出力の桁揃えに使う。
`std::setw` は次の 1 回の出力だけに効く。

```cpp
std::cout << std::setw(6) << 42 << '\n';
std::cout << 42 << '\n'; // こちらは元に戻る
```

## std::setfill

幅が足りないときに埋める文字を設定する。
`std::setw` と組み合わせて使うことが多い。

```cpp
std::cout << std::right << std::setw(8) << std::setfill('.') << 42 << '\n';
std::cout << std::left << std::setw(8) << "cat" << '\n';
```

## std::setprecision

浮動小数点数の精度を設定する。
`<iomanip>`ヘッダで提供され、表示する桁数を調整したいときに使う。

- 通常時は有効桁数を調整する
- `std::fixed` / `std::scientific` と組み合わせると小数部桁数を調整する

```cpp
std::cout << std::setprecision(3) << 123.456 << '\n';
std::cout << std::fixed << std::setprecision(3) << 123.456 << '\n';
```

## 関連

- [[標準入力（C++）]]
- [[標準出力（C++）]]
- [[標準ストリーム（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/output-with-ostream-and-ios/
- [cpprefjp: std::ws](https://cpprefjp.github.io/reference/istream/ws.html)
- [cpprefjp: std::hex](https://cpprefjp.github.io/reference/ios/hex.html)
- [cpprefjp: std::setw](https://cpprefjp.github.io/reference/iomanip/setw.html)
- [cpprefjp: std::setprecision](https://cpprefjp.github.io/reference/iomanip/setprecision.html)
