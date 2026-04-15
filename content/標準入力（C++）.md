---
publish: true
tags:
  - CPlusPlus
---
C++ で標準入力を表すのが `std::cin` である。
`std::cin` は入力[[ストリーム]]オブジェクトで、キーボードなどから届いた入力を順に読み取る。

## 基本

- 数値や単語を読むときは[[抽出演算子]] `>>` を使う
- 1 行全体を読むときは[[getline（C++）]]を使う
- 空白や改行も含めて生の形で読みたいときは[[非書式化入力関数]]を使う
- `>>` は既定で先頭の空白文字を読み飛ばす

```cpp
#include <iostream>

int main()
{
    int number {};
    std::cin >> number;
}
```

## 空白の扱い

`std::cin >> value` は、読み取りを始める前にスペース・タブ・改行を読み飛ばす。
その後、型に応じて値を解釈し、次の空白文字の手前で止まる。

たとえば文字列への抽出では、`hello world` を入力すると最初の `hello` だけが読み取られ、空白以降はストリームに残る。

## 入力が残る

`>>` で数値を読んだあと、確定に使った改行文字 `'\n'` はストリームに残ることがある。
そのため、続けて[[getline（C++）]]で 1 行読みたい場合は、残っている改行を先に処理する必要がある。

```cpp
#include <iostream>
#include <limits>
#include <string>

int main()
{
    int number {};
    std::cout << "Enter a number: ";
    std::cin >> number;
    std::cout << "You entered: " << number << '\n';

    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::string line {};
    std::cout << "Enter a line: ";
    std::getline(std::cin, line);
    std::cout << "You entered: " << line << '\n';
}
```

`ignore(max, '\n')` の詳細は[[ストリーム状態と入力検証（C++）]]を参照。

## 関連

- [[標準ストリーム（C++）]]
- [[ストリーム（C++）]]
- [[抽出演算子]]
- [[非書式化入力関数]]
- [[getline（C++）]]
- [[ストリーム状態と入力検証（C++）]]
- [[マニピュレータ（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/input-with-istream/
- https://www.learncpp.com/cpp-tutorial/stdcin-and-handling-invalid-input/
