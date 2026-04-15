---
publish: true
tags:
  - CPlusPlus
---
`std::weak_ptr` は、`<memory>` ヘッダで提供される[[スマートポインタ]]である。

`std::shared_ptr` が管理しているオブジェクトを参照できるが、[[所有権]]は持たない。
そのため、`std::shared_ptr` の所有者数には数えられない。

## 何のために使うか

主な用途は、[[循環参照]]を防ぐことである。

`std::shared_ptr` 同士が互いを所有すると、参照カウントが 0 にならず、オブジェクトが解放されないことがある。
その輪のどこかを `std::weak_ptr` にすると、所有の循環を断ち切れる。

## 使い方

`std::weak_ptr` は、そのままでは `*` や `->` で直接使えない。
アクセスしたいときは `lock()` で一時的に `std::shared_ptr` を作る。

```cpp
std::weak_ptr<Person> partner;

if (auto p = partner.lock())
{
    // p は std::shared_ptr<Person>
}
```

`lock()` が失敗した場合は、空の `std::shared_ptr` が返る。
これは管理対象がすでに破棄されていることを意味する。

## 有効性の確認

`expired()` を使うと、参照先がすでに破棄されたかどうかを調べられる。

```cpp
if (!partner.expired())
{
}
```

ただし、実際に使うときは `expired()` を先に見るより、`lock()` して使えるかどうかをその場で確認するほうが自然なことが多い。

## 補足

- `std::weak_ptr` 単体では所有権を持たないので、オブジェクトの寿命は延ばさない
- `std::shared_ptr` の補助として使う型であり、単独の所有者型ではない

## 関連

- [[スマートポインタ]]
- [[shared_ptr]]
- [[循環参照]]
- [[所有権]]

## 参考

- https://www.learncpp.com/cpp-tutorial/circular-dependency-issues-with-stdshared_ptr-and-stdweak_ptr/
- https://cpprefjp.github.io/reference/memory/weak_ptr.html
