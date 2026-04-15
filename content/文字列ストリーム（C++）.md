---
publish: true
tags:
  - CPlusPlus
---
`<sstream>` ヘッダで提供される、文字列用の[[ストリーム]]。
キーボードや画面の代わりに「文字列」を入出力先として扱える。

## 主な型

- `std::istringstream`
  文字列を入力元として読む
- `std::ostringstream`
  文字列へ出力する
- `std::stringstream`
  文字列に対して読み書きの両方を行う

通常は、読み取り専用なら `istringstream`、出力専用なら `ostringstream`、両方必要なら `stringstream` を使う。

## 何に使うか

- 文字列を数値へ変換する
- 数値や値を文字列へ整形する
- 1 行読み込んだ文字列を、さらに単語ごとに分解する
- 出力を一度バッファして、あとでまとめて使う

## 文字列を読み取る

```cpp
#include <sstream>

std::istringstream input{ "123 45.6" };

int n {};
double d {};
input >> n >> d;
```

`std::cin` も `std::istringstream` も `std::istream` 系の入力ストリームなので、[[抽出演算子]] `>>` による書式化入力の基本挙動は共通する。

## 文字列へ書き出す

```cpp
#include <sstream>

std::ostringstream output {};
output << "score: " << 42;

std::string result { output.str() };
```

`str()` を使うと、ストリーム内部の文字列バッファ全体を取り出せる。

## `str()` で設定・取得する

文字列ストリームには、文字を `<<` で流し込むだけでなく、`str()` でバッファ全体を直接設定することもできる。

```cpp
std::stringstream ss {};
ss.str("en garde!");
```

逆に、現在のバッファ全体を取得したいときも `str()` を使う。

```cpp
std::stringstream ss {};
ss << "12345 67.89";

std::string whole { ss.str() };
```

`>>` は次の値を順番に取り出すが、`str()` はストリーム全体の内容を返す。

## 文字列と数値の相互変換

```cpp
std::stringstream convert1 {};
convert1 << 123 << ' ' << 45.6;

std::string a {};
std::string b {};
convert1 >> a >> b;

std::stringstream convert2 {};
convert2 << "123 45.6";

int n {};
double d {};
convert2 >> n >> d;
```

ただし、単純な数値変換だけなら `std::from_chars` や `std::to_chars`、文字列化だけなら `std::to_string` などの方が適することもある。
`stringstream` の強みは、ストリームとして同じ書き方で柔軟に扱える点にある。

## 再利用するとき

文字列ストリームを再利用するなら、バッファだけでなく状態フラグも戻すのが安全。

```cpp
std::stringstream ss {};
ss << "Hello";

ss.str("");   // バッファを空にする
ss.clear();   // エラーフラグをリセットする

ss << "World";
```

`str("")` だけでは `failbit` などの状態は戻らないため、読み書きに失敗したあとに再利用するなら `clear()` も合わせて行う。

## 関連

- [[ストリーム（C++）]]
- [[抽出演算子]]
- [[挿入演算子]]
- [[ストリーム状態と入力検証（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/stream-classes-for-strings/
- https://en.cppreference.com/w/cpp/io/basic_stringstream
