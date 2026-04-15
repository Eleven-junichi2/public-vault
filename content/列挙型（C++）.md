---
publish: true
tags:
  - CPlusPlus
---
enumeration。
関連する定数の集合に名前を付けて、1つの独立した型として扱えるようにしたもの。
列挙型が持つ個々の定数を **列挙子（enumerator）** という。

## スコープなし列挙型

unscoped enumeration。`enum` キーワードで定義する。
C言語の列挙型に近く、列挙子は列挙型の外側のスコープにも公開される。

```cpp
enum Color
{
    red,
    green,
    blue,
};
```

```cpp
Color apple { red };
Color shirt { green };
```

列挙子が現在のスコープに直接入るため、[[名前の衝突（C++）]]を起こしやすい。避けるには、`namespace` に入れて使い分ける。

### 列挙子の値

列挙子には、明示的に値を指定しない限り `0` から順に整数値が割り当てられる。

```cpp
enum Pet
{
    cat,   // 0
    dog,   // 1
    pig,   // 2
    whale, // 3
};
```

必要なら明示的に値を指定できる。

```cpp
enum HttpStatus
{
    ok = 200,
    notFound = 404,
};
```

明示的な値指定は、外部仕様と対応づけたいときや、値そのものに意味があるときに使う。

### 整数との変換

スコープなし列挙型は整数型へ暗黙変換される。

```cpp
enum Pet
{
    cat,
    dog,
    pig,
    whale,
};

int petId { cat }; // ok
```

一方、整数から列挙型への暗黙変換はできない。
整数を列挙型へ変換したい場合は、[[static_cast]]で明示的に変換する。

```cpp
Pet pet { static_cast<Pet>(2) };
```

ただし、このような変換で得た値が有効な列挙子に対応しているとは限らないため、外部入力をそのまま列挙型へ変換するときは注意が必要である。

### 例

```cpp
enum FileReadResult
{
    readResultSuccess,
    readResultErrorFileOpen,
    readResultErrorFileRead,
    readResultErrorFileParse,
};

FileReadResult readFileContents()
{
    if (!openFile())
        return readResultErrorFileOpen;
    if (!readFile())
        return readResultErrorFileRead;
    if (!parseFile())
        return readResultErrorFileParse;

    return readResultSuccess;
}
```

### ビットフラグとしての利用

スコープなし列挙型は整数型へ暗黙変換されるため、ビットフラグと組み合わせて使われることがある。
ただし、現代のC++では、名前衝突や暗黙変換の問題を避けるために、スコープ付き列挙型を明示的な変換付きで使うことも多い。

### 列挙子と文字列の変換

C++標準ライブラリには、列挙子と文字列を相互変換する仕組みは標準では用意されていない。
必要なら `switch` や `if` で自分で実装する。

```cpp
#include <optional>
#include <string_view>

enum Pet
{
    cat,
    dog,
    pig,
    whale,
};

constexpr std::string_view getPetName(Pet pet)
{
    switch (pet)
    {
    case cat:   return "cat";
    case dog:   return "dog";
    case pig:   return "pig";
    case whale: return "whale";
    default:    return "???";
    }
}

constexpr std::optional<Pet> getPetFromString(std::string_view sv)
{
    if (sv == "cat")   return cat;
    if (sv == "dog")   return dog;
    if (sv == "pig")   return pig;
    if (sv == "whale") return whale;

    return {};
}
```

## スコープ付き列挙型

scoped enumeration。`enum class` キーワードで定義する。

```cpp
enum class Color
{
    red,
    green,
    blue,
};
```

スコープ付き列挙型は、スコープなし列挙型と比べて次の特徴を持つ。

- 列挙子は列挙型のスコープ内にあるため、`Color::red` のように参照する
- 整数型へ暗黙変換されない
- 異なる列挙型同士や整数との混同が起こりにくい

### 例

```cpp
#include <iostream>

enum class Weather : unsigned short
{
    sunny,
    cloudy,
    rainy,
};

int main()
{
    Weather current { Weather::cloudy };

    switch (current)
    {
    case Weather::sunny:
        std::cout << "It's sunny!\n";
        break;
    case Weather::cloudy:
        std::cout << "It's cloudy.\n";
        break;
    case Weather::rainy:
        std::cout << "It's rainy.\n";
        break;
    }
}
```

### `using enum`

C++20 では、`using enum 列挙型名;` と書くことで、列挙子を現在のスコープに導入できる。

```cpp
enum class Color
{
    red,
    green,
    blue,
};

using enum Color;

Color c { red };
```

ただし、スコープ付き列挙型の名前衝突回避という利点を弱めるため、使いどころは限定される。

## 基底型

列挙子の値を表現するための整数型を、基底型（underlying type）という。

基底型は明示的に指定できる。

```cpp
enum Color : std::int8_t
{
    red,
    green,
    blue,
};
```

```cpp
enum class Weather : unsigned short
{
    sunny,
    cloudy,
    rainy,
};
```

スコープなし列挙型では、基底型を指定しない場合の選択は実装に委ねられる。
多くの環境では `int` に近い型になるが、常にそうとは限らない。

## 参考

- https://www.learncpp.com/cpp-tutorial/unscoped-enumerations/
- https://www.learncpp.com/cpp-tutorial/unscoped-enumerator-integral-conversions/
- https://www.learncpp.com/cpp-tutorial/converting-an-enumeration-to-and-from-a-string/
- https://www.learncpp.com/cpp-tutorial/scoped-enumerations-enum-classes/
