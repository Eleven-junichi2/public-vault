---
publish: true
tags:
  - CPlusPlus
---
declarative region。ある[[宣言（C++）]]によって名前が導入される領域のこと。
[[スコープ（C++）]]がその名前を参照できる範囲であるのに対して、宣言領域はその名前が属する領域を表す。

```cpp
void example() // この例では、exampleの宣言領域はグローバル名前空間
{
	int hoge = 10; // hogeの宣言領域はこのブロック
}
```

## 関連

- [[ブロック（C++）]]
- [[名前空間（C++）]]

## 参考

- https://onihusube.hatenablog.com/entry/2023/01/14/012738#%E5%AE%A3%E8%A8%80%E9%A0%98%E5%9F%9F
