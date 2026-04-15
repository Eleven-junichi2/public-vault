---
publish: true
tags:
  - CPlusPlus
---
入れ子になった[[if文（C++）]]で、`else`がどの`if`に対応するかが読み手にとって曖昧になりやすい問題。
構文上は、`else`はもっとも近い`if`に結び付く。

```cpp
if (a <= 10)
    if (a <= 5)
        std::cout << a << "<=5\n";
else
    std::cout << a << "> 5\n";
```

## 関連

- [[if文（C++）]]

## 参考

- https://www.learncpp.com/cpp-tutorial/common-if-statement-problems/
