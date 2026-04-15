---
publish: true
tags:
  - CPlusPlus
---
forward declaration。[[定義（C++）]]より前に名前を[[宣言（C++）]]して、後でその定義を置けるようにすること。
関数やクラスなどで用いられる。

```cpp
#include <iostream>

int add(int x, int y); // forward declaration of add() (using a function declaration)

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n'; // this works because we forward declared add() above
    return 0;
}

int add(int x, int y) // even though the body of add() isn't defined until here
{
    return x + y;
}
```

```cpp
class Foo; // クラスの前方宣言
```

## 参考

- https://www.learncpp.com/cpp-tutorial/forward-declarations/
