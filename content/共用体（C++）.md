---
publish: true
---

#C-plus-plus 

```c++
#include <iostream>
using namespace std;

union U
{
    int a;
    int b;
    int c;
};

int main(int argc, char const *argv[])
{
    U u = { 22 };
    cout << "&u.a: " << &u.a << endl;
    cout << "&u.b: " << &u.b << endl;
    cout << "&u.c: " << &u.c << endl;
    cout << "u.a: " << u.a << endl;
    cout << "u.b: " << u.b << endl;
    u.a = 11;
    cout << "`u.a = 11`" << endl;
    cout << "u.c: " << u.c << endl;
    return 0;
}

/*
❯ ./union 
&u.a: 0x16f9be9dc
&u.b: 0x16f9be9dc
&u.c: 0x16f9be9dc
*/
```

## 無名共用体

同じアドレスのメンバを作ることができる。
無名共用体で定義されたメンバのスコープは、その無名共用体が宣言されたスコープと同じとみなされる。
