---
publish: true
tags:
  - CPlusPlus
---
`std::shared_ptr` は、`<memory>` ヘッダで提供される[[スマートポインタ]]である。

1つのオブジェクトの[[所有権]]を、複数の `std::shared_ptr` で共有できる。
最後の所有者がいなくなったときに、管理対象は破棄される。

## 仕組み

`std::shared_ptr` は、典型的には参照カウントを使って管理する。

- コピーすると所有者数が増える
- 破棄されると所有者数が減る
- 所有者数が 0 になると管理対象が破棄される

## 例

```cpp
#include <iostream>
#include <memory>

class Resource
{
public:
    Resource() { std::cout << "Resource acquired\n"; }
    ~Resource() { std::cout << "Resource destroyed\n"; }
};

int main()
{
    auto p1 { std::make_shared<Resource>() };
    {
        auto p2 { p1 };
        std::cout << "One more owner exists\n";
    }

    std::cout << "Still alive\n";
}
```

このとき `p1` と `p2` は同じオブジェクトを共有しており、最後の `shared_ptr` がなくなるまで管理対象は破棄されない。

## `make_shared`

`std::shared_ptr` を作るときは、通常 `std::make_shared` を使う。

```cpp
#include <memory>

class Resource {};

auto ptr { std::make_shared<Resource>() };
```

`std::shared_ptr<T>{ new T{} }` と直接書くより、次の点で使いやすい。

- `new` を直接書かずに済むので簡潔である
- `shared_ptr` に所有させたいことが分かりやすい
- コントロールブロックと管理対象を効率よく確保できることが多い

そのため、特別な理由がなければ `std::make_shared` を使うほうが自然である。

## 注意

同じ生ポインタから、独立に複数の `std::shared_ptr` を作ってはいけない。

```cpp
Resource* raw { new Resource{} };
std::shared_ptr<Resource> p1 { raw };
std::shared_ptr<Resource> p2 { raw }; // 危険
```

このようにすると、別々の管理情報が作られ、二重解放の原因になる。
共有したいなら、既存の `std::shared_ptr` をコピーする。

## `unique_ptr` との関係

`std::unique_ptr` から `std::shared_ptr` へは、[[ムーブ]]によって所有権を移せる。

```cpp
std::unique_ptr<Resource> up { std::make_unique<Resource>() };
std::shared_ptr<Resource> sp { std::move(up) };
```

一方で、`std::shared_ptr` から `std::unique_ptr` へ安全に戻すことはできない。

## 補足

- 複数所有が本当に必要なときだけ使うほうが分かりやすい
- 循環参照があると、参照カウントが 0 にならず解放されないことがある
- そのような場面では [[weak_ptr]] を使う

## 関連

- [[スマートポインタ]]
- [[unique_ptr]]
- [[weak_ptr]]
- [[循環参照]]

## 参考

- https://www.learncpp.com/cpp-tutorial/stdshared_ptr/
- https://cpprefjp.github.io/reference/memory/shared_ptr.html
