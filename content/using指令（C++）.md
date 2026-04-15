---
publish: true
tags:
  - CPlusPlus
---
using-directive。構文:`using namespace 名前空間の識別子;`
指定した[[名前空間（C++）]]を、名前空間名を書かずに使う名前の探索対象に加える。
そのため、その名前空間の名前を所属する名前空間を省略して使えるようになる。

[[using宣言（C++）]]とは異なるので注意。

具体的には、コンパイラが識別子の名前解決をする際、それを行う現在の[[スコープ（C++）]]で識別子が見つからない時、この指令で指定された[[名前空間（C++）]]も探す挙動になる。

```c++
using namespace namespace-name;

// ネストした内側のみを省略する
using namespace namespace-name::nested-name;
```

```cpp
#include <iostream> // std名前空間でcoutの宣言をする内容に置換

using namespace std; //　std::coutにcoutでアクセスできるようになる

int main()
{
    cout << "Hello, world!";
    return 0;
}
```
