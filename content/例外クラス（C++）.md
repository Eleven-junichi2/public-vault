---
publish: true
tags:
  - CPlusPlus
---
exception class。

[[例外処理（C++）]]で送出するために設計された[[クラス型（C++）]]。

## 概要

`int`や`const char*`のような基本型を例外として送出することもできるが、それだけでは何が起きたのかが曖昧になりやすい。

[[例外クラス（C++）|例外クラス]]を使うと、

- 何の種類の例外かを型で区別できる
- エラーメッセージなどの追加情報を持たせられる
- 例外ごとに異なる`catch`で処理できる

## 例

```cpp
class ArrayException
{
private:
    std::string m_error{};

public:
    ArrayException(std::string_view error)
        : m_error{ error }
    {
    }

    const std::string& getError() const
    {
        return m_error;
    }
};
```

```cpp
if (index < 0 || index >= getLength())
    throw ArrayException{ "Invalid index" };
```

このように、例外クラスを送出すると、どのクラスから発生したどの種類の異常かを表現しやすくなる。

## 受け取り方

クラス型の例外は、通常`const`参照で受け取る。

```cpp
catch (const ArrayException& exception)
{
    std::cerr << exception.getError() << '\n';
}
```

これは不要なコピーを避けるためであり、[[オブジェクトスライシング]]を防ぐ意味もある。  
ポインタで受け取る方法は、特別な理由がない限り通常は使わない。

## 継承との関係

例外クラスも通常のクラスと同じように[[継承（C++）]]できる。  
そのため、基底例外クラスを作り、その派生例外クラスをまとめて扱うことができる。

```cpp
class Base {};
class Derived : public Base {};

try
{
    throw Derived{};
}
catch (const Base&)
{
    std::cerr << "caught Base";
}
catch (const Derived&)
{
    std::cerr << "caught Derived";
}
```

この例では`Derived`が送出されても、先に`catch (const Base&)`が一致するため、`Derived`用の`catch`には到達しない。

そのため、派生例外クラス用の`catch`は、基底例外クラス用の`catch`より先に書く必要がある。

## std::exception

標準ライブラリの多くの例外クラスは、`<exception>`ヘッダの`std::exception`を基底クラスとしている。

そのため、

```cpp
catch (const std::exception& exception)
{
    std::cerr << exception.what() << '\n';
}
```

のように書くことで、標準ライブラリ由来の多くの例外をまとめて受け取れる。

`std::exception`には仮想関数`what()`があり、例外の説明文字列を返す。  
多くの派生例外クラスはこの`what()`をオーバーライドしている。

## 独自例外クラスをstd::exceptionから派生させる

独自例外クラスも`std::exception`や`std::runtime_error`から派生させることができる。

```cpp
class ArrayException : public std::runtime_error
{
public:
    ArrayException(const std::string& error)
        : std::runtime_error{ error }
    {
    }
};
```

`std::runtime_error`を使うと、エラーメッセージの保持や`what()`の実装を自分で書かずに済む。

一方、`std::exception`から直接派生する場合は、必要に応じて`what() const noexcept`をオーバーライドする。

## 関連

- [[例外処理（C++）]]
- [[std::exception]]
- [[std::runtime_error]]

## 参考

- https://www.learncpp.com/cpp-tutorial/exceptions-classes-and-inheritance/
