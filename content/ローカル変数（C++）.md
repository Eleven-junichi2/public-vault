---
publish: true
tags:
  - CPlusPlus
---
[[関数（C++）]]内など[[ブロック（C++）]]の中に定義された[[変数（C++）]]。
多くは、その[[生存期間（C++）]]が[[ブロック（C++）]]の終わりまで続く。
ただし、`static`ローカル変数のような例外もある。

通常は、そのブロックの中でのみ使える。

デフォルトで[[リンケージ]]を持たない。（no linkage）

```cpp
int add(int x, int y)
{
    int z{ x + y };

    return z;
} // zの生存期間はここまで
```


ネストされたスコープでは、内側のスコープから外側の名前を参照できるが、逆はできない。

リンケージの話の例:
```cpp
int main()
{
    int x { 2 }; // local variable, no linkage

    {
        int x { 3 }; // 先のx別
    }

    return 0;
}
```

## 参考

- https://www.learncpp.com/cpp-tutorial/local-variables/
