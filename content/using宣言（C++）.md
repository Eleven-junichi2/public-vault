---
publish: true
tags:
  - CPlusPlus
---

型に別名(エイリアス=alias)を与えることができる。
このエイリアスは、[[非修飾名]]か、特定の名前を指定することができる。

```cpp
#include <iostream>

int main()
{
   using std::cout; // this using declaration tells the compiler that cout should resolve to std::cout
   cout << "Hello world!\n"; // so no std:: prefix is needed here!

   return 0;
} // the using declaration expires at the end of the current scope
```

```c++
#include <iostream>

using happyint = int;

int main(int argc, char const *argv[])
{
    happyint lucky = 777;
    int unlucky = 666;
    std::cout << lucky + unlucky << std::endl;
    return 0;
}
```

## 参考

- https://www.learncpp.com/cpp-tutorial/using-declarations-and-using-directives/