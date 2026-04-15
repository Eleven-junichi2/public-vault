---
publish: true
tags:
  - CPlusPlus
---
`extern`キーワード。[[外部リンケージ]]を持つ名前を、別の[[翻訳単位]]から参照するための[[宣言（C++）]]に用いられる。
特に、[[外部変数]]を定義せずに宣言だけしたいときに使う。

```cpp
// a.cpp
int g_value{ 42 }; // 定義

// b.cpp
extern int g_value; // 宣言
int main()
{
    return g_value;
}
```

変数では、`extern`付きの宣言だけでは[[定義（C++）]]にならないため、どこか1か所に定義が必要。
関数宣言は通常 `extern` を明示しなくても外部リンケージを持つため、変数ほどは書かれない。

## 参考

- https://www.learncpp.com/cpp-tutorial/external-linkage-and-variable-forward-declarations/
