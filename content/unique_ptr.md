---
publish: true
tags:
  - CPlusPlus
---
`std::unique_ptr` は、`<memory>` ヘッダで提供される[[スマートポインタ]]である。

1つのオブジェクトの[[所有権]]をただ1つだけ持つ。
コピーはできず、[[ムーブ]]によって所有権を別の `std::unique_ptr` へ移せる。

## 基本

通常は、共有しない動的オブジェクトの管理に使う。

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
    std::unique_ptr<Resource> ptr { new Resource{} };
}
```

スコープを抜けると、`ptr` のデストラクタによって管理対象も自動で破棄される。

## `make_unique`

`std::unique_ptr` を作るときは、通常 `std::make_unique` を使う。

```cpp
#include <memory>

int main()
{
    auto ptr { std::make_unique<int>(5) };
}
```

`std::make_unique` を使う理由は次のとおりである。

- `new` を直接書かずに済むので簡潔である
- 一時的な生ポインタを露出させずに書ける
- `std::unique_ptr` に所有させたいことがその場で分かりやすい

そのため、特別な理由がなければ `std::make_unique` を使うほうが自然である。

## アクセス

`std::unique_ptr` は `*` と `->` で管理対象にアクセスできる。

```cpp
#include <iostream>
#include <memory>

class Resource
{
public:
    void say() const
    {
        std::cout << "hello\n";
    }
};

int main()
{
    auto ptr { std::make_unique<Resource>() };

    if (ptr)
        ptr->say();
}
```

生ポインタが必要な場面では `get()` で取り出せる。
ただし、`get()` で得たポインタは所有権を持たない。

## 所有権の移動

`std::unique_ptr` はコピーできないので、別の `std::unique_ptr` に渡すときは通常 `std::move` を使う。

```cpp
#include <memory>
#include <utility>

int main()
{
    auto p1 { std::make_unique<int>(5) };
    auto p2 { std::move(p1) };
}
```

このあと `p1` は空になり、所有権は `p2` に移る。

## 関数とのやりとり

関数が[[所有権]]を受け取るなら、`std::unique_ptr` を値渡しする。

```cpp
#include <memory>

class Resource {};

void takeOwnership(std::unique_ptr<Resource> res);
```

単に使うだけなら、管理対象への参照やポインタを渡すほうが自然なことが多い。

```cpp
#include <memory>

class Resource {};

void useResource(const Resource& res);
```

また、`std::unique_ptr` は関数から値で安全に返せる。

```cpp
#include <memory>

class Resource {};

std::unique_ptr<Resource> createResource()
{
    return std::make_unique<Resource>();
}
```

このように返すと、[[所有権]]を安全に呼び出し側へ渡せる。

## 補足

- 配列用の `std::unique_ptr<T[]>` もある
- まず所有者として `std::unique_ptr` を考えるのが、現代の C++ では自然なことが多い

## 関連

- [[スマートポインタ]]
- [[shared_ptr]]
- [[ムーブ]]
- [[所有権]]

## 参考

- https://www.learncpp.com/cpp-tutorial/stdunique_ptr/
