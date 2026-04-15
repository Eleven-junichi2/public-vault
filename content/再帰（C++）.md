---
publish: true
tags:
  - CPlusPlus
---
関数がその処理の中で自身を呼び出すことを再帰という。

再帰では、処理を止めるための終了条件が必要である。
終了条件がないと、呼び出しが続いて停止しない。

```cpp
int sumTo(int x)
{
    if (x <= 0)
        return 0; // 終了条件

    return x + sumTo(x - 1); // 再帰呼び出し
}
```

## 参考

- https://www.learncpp.com/cpp-tutorial/recursion/
