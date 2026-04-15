---
publish: true
tags:
  - CPlusPlus
---
C++では、時間や時間間隔を扱う標準ライブラリとして`<chrono>`を提供している。

時間計測では、主に次の3つを使う。

- クロック: 現在時刻を取得する
- `time_point`: 時間軸上の一点を表す
- `duration`: 時間の長さを表す

## 時間計測の基本

処理時間を測るときは、開始時刻と終了時刻を取得し、その差を取る。

```cpp
#include <chrono>
#include <iostream>

int main()
{
    const auto start { std::chrono::steady_clock::now() };

    // 計測したい処理

    const auto end { std::chrono::steady_clock::now() };
    const auto elapsed { end - start };

    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(elapsed).count()
              << " ms\n";
}
```

`end - start` の結果は `duration` になる。
`count()` で数値として取り出せる。

## どのクロックを使うか

### `steady_clock`

処理時間の計測では、通常 `std::chrono::steady_clock` を使う。
`steady_clock` は時間が逆行しないクロックであり、システム時刻の変更の影響を受けにくい。

### `system_clock`

`std::chrono::system_clock` はシステム時刻を表すクロックである。
現在日時を扱いたいときには便利だが、ユーザーやOSによる時刻変更の影響を受けうるため、純粋な処理時間の計測には向かないことがある。

### `high_resolution_clock`

`std::chrono::high_resolution_clock` は高い分解能を持つクロックだが、処理系によって `system_clock` または `steady_clock` の別名として実装されることがある。
そのため、時間計測では名前だけで選ばず、逆行しないことが重要なら `steady_clock` を使うほうが分かりやすい。

## 単位変換

`duration_cast` を使うと、経過時間を任意の単位へ変換できる。

```cpp
const auto elapsed_us { std::chrono::duration_cast<std::chrono::microseconds>(elapsed) };
const auto elapsed_ms { std::chrono::duration_cast<std::chrono::milliseconds>(elapsed) };
```

秒を小数で扱いたい場合は、`std::chrono::duration<double>` を使う書き方もある。

```cpp
const std::chrono::duration<double> elapsed_sec { end - start };
std::cout << elapsed_sec.count() << " s\n";
```

## 補足

- 短い処理は1回だけ測ると誤差が出やすい
- コンパイラ最適化や実行環境によって計測結果は変わる
- ベンチマークでは、複数回測定して傾向を見るほうがよい

## 参考

- https://cpprefjp.github.io/reference/chrono.html
- https://cpprefjp.github.io/reference/chrono/steady_clock.html
- https://cpprefjp.github.io/reference/chrono/high_resolution_clock.html
- https://cpprefjp.github.io/reference/chrono/system_clock.html
- https://www.learncpp.com/cpp-tutorial/timing-your-code/
