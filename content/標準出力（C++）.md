---
publish: true
tags:
  - CPlusPlus
---
C++ で標準出力を表すのが `std::cout` である。
通常の実行結果やユーザー向けメッセージは、まず `std::cout` へ出力する。
`std::cout` は単なる出力先ではなく、書式設定の状態を保持する `std::ostream` オブジェクトでもある。

## 基本

```cpp
#include <iostream>

int main()
{
    int value { 42 };
    std::cout << "value = " << value << '\n';
}
```

値の出力には[[挿入演算子]] `<<` を使う。
演算子は `std::ostream&` を返すため、`std::cout << a << b;` のように連結できる。

## 書式設定は状態として残る

`std::cout` に適用した書式設定の多くは、そのストリームの状態として保持される。
そのため、`std::hex` や `std::boolalpha` を一度設定すると、明示的に戻すまで後続の出力にも影響する。

```cpp
std::cout << std::boolalpha << true << '\n';
std::cout << false << '\n'; // ここでも false と出る

std::cout << std::hex << 27 << '\n';
std::cout << 28 << '\n'; // ここでも 16 進数のまま
```

詳しい調整方法は[[マニピュレータ（C++）]]を参照。

## バッファリング

`std::cout` は多くの環境で[[バッファ]]を使って出力する。
そのため、書き込んだ内容はすぐには画面へ現れず、まとまって送られることがある。

## `'\n'` と `std::endl`

- `'\n'`
  改行文字だけを出力する
- `std::endl`
  改行に加えて[[フラッシュ]]も行う

改行だけで十分なら `'\n'` の方が軽いことが多い。
即時反映したいときだけ `std::endl` や `std::flush` を使う。

## 書式設定

出力書式は[[マニピュレータ（C++）]]で調整できる。
複数の設定を重ねることもできる。

```cpp
#include <iomanip>
#include <iostream>

int main()
{
    std::cout << std::boolalpha << true << '\n';
    std::cout << std::hex << 27 << '\n';
    std::cout << std::dec << std::fixed << std::setprecision(2) << 3.14159 << '\n';
    std::cout << std::setw(8) << std::setfill('.') << 42 << '\n';
}
```

## `std::setprecision`

`std::setprecision(n)` の意味は、出力モードによって少し変わる。

- 通常時
  有効桁数を指定する
- `std::fixed` や `std::scientific` と併用したとき
  小数部の桁数を指定する

```cpp
std::cout << std::setprecision(3) << 123.456 << '\n';              // 有効桁数
std::cout << std::fixed << std::setprecision(3) << 123.456 << '\n'; // 小数部 3 桁
```

## 関連

- [[標準ストリーム（C++）]]
- [[標準エラー出力（C++）]]
- [[挿入演算子]]
- [[マニピュレータ（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/output-with-ostream-and-ios/
