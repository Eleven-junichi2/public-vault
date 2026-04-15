---
publish: true
tags:
  - CPlusPlus
---
[[ストリーム（C++）]]は、読み書きの結果に応じて状態フラグを持つ。
入力検証では、特に `failbit` をどう扱うかが重要になる。

## 主な状態フラグ

- `goodbit`
  正常な状態。
- `failbit`
  型変換失敗などの非致命的なエラー。
- `badbit`
  デバイス異常などの致命的なエラー。
- `eofbit`
  入力元の終端に到達した状態。

## 状態確認

- `good()`
  正常なら `true`
- `fail()`
  `failbit` または `badbit` が立つと `true`
- `bad()`
  致命的エラーなら `true`
- `eof()`
  終端到達なら `true`
- `rdstate()`
  現在の状態フラグを返す

`if (std::cin >> value)` のように書けるのは、抽出後のストリームが真偽値文脈で評価できるため。
成功していて `fail()` でないときは真、失敗しているときは偽として扱える。

## 復旧でよく使う関数

- `clear()`
  状態フラグをクリアして、再び読み取り可能にする
- `ignore(count, delim)`
  指定文字数または区切り文字まで入力を捨てる
- `gcount()`
  直前の非書式化入力で読んだ文字数を返す
- `peek()`
  次の 1 文字を消費せずに確認する

`std::cin` は、型変換できない値の入力などで抽出に失敗すると `failbit` が立ち、そのままでは以降の入力も失敗する。
そのため、入力の立て直しでは次の 2 段階を行うことが多い。

1. `clear()` で失敗状態を解除する
2. `ignore()` で問題のある入力を捨てる

```cpp
#include <iostream>
#include <limits>

int readNumber()
{
    while (true)
    {
        std::cout << "Enter an integer: ";
        int value {};

        if (std::cin >> value)
        {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return value;
        }

        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Please enter a valid integer.\n";
    }
}
```

## `clear()`

`clear()` は、何も引数を渡さなければ状態フラグを正常状態へ戻す。

```cpp
std::cin.clear();
```

引数付きで使うと、状態を明示的に設定することもできる。

```cpp
std::cin.clear(std::ios::goodbit);
```

通常の入力復旧では、引数なしの `clear()` を使えば十分なことが多い。

## `ignore()` の使いどころ

```cpp
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
```

これは「改行が来るまで、あるいは十分大きな上限まで入力を捨てる」という意味で、残りの行全体を捨てたいときの定番。
単なる `std::cin.ignore()` は 1 文字しか捨てないため、復旧用途では足りないことがある。

`ignore()` のあとには `gcount()` を使って、実際に何文字読み飛ばしたか確認できる。

```cpp
std::cin.ignore(5, '\n');
std::streamsize ignored { std::cin.gcount() };
```

## 入力検証

入力検証は大きく 2 つに分けて考えると整理しやすい。

- 形式の検証
  そもそも整数として読めるか、期待した書式か
- 値域の検証
  読めた値が許された範囲に収まるか

```cpp
int guess {};
if (!(std::cin >> guess))
{
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}
else if (guess < 1 || 10 < guess)
{
    std::cout << "Out of range.\n";
}
```

## `gcount()`

`gcount()` は、`get()`、`getline()`、`ignore()` などの非書式化入力関数の直後に、何文字処理したかを確認するときに使う。
[[抽出演算子]] `>>` や自由関数の[[getline（C++）]]では基本的に使わない。

## `peek()`

`peek()` は、次に読まれる 1 文字を消費せずに確認したいときに使う。

```cpp
int ch { std::cin.peek() };
if (ch == '\n')
    std::cout << "next is newline\n";
```

入力検証や簡単な先読みが必要なときに便利。

## EOF と失敗状態

入力終端に到達すると `eofbit` が立つ。
さらに、終端で必要な値を読み取れなかった場合は `failbit` も同時に立つことがある。

そのため、EOF は「終端到達」と「読み取り失敗」が重なって見える場合がある。

一方、`badbit` はより深刻な入出力エラーを表し、通常の対話入力では `failbit` ほど頻繁には出ない。

## 関連

- [[標準入力（C++）]]
- [[抽出演算子]]
- [[getline（C++）]]
- [[非書式化入力関数]]

## 参考

- https://www.learncpp.com/cpp-tutorial/stream-states-and-input-validation/
- https://www.learncpp.com/cpp-tutorial/stdcin-and-handling-invalid-input/
