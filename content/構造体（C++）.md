---
publish: true
tags:
  - CPlusPlus
---
struct。
メンバの[[アクセス指定子]]がデフォルトで `public` である[[クラス型（C++）]]。

C++では、構造体もクラスの一種であり、データメンバだけでなく[[メンバ関数]]、[[コンストラクタ（C++）]]、[[アクセス指定子]]なども持てる。

## 定義

```cpp
struct Employee
{
    int id {};
    int age {};
    double wage {};
};
```

各メンバには、[[デフォルトメンバ初期化子]]を書いて初期値を設定できる。

## オブジェクトの作成

```cpp
Employee e1 {};
Employee e2 { 1, 32, 60000.0 };
```

構造体が[[集成体]]である場合は、`{}` を使って各メンバを順番に初期化できる。

## メンバアクセス

オブジェクトのメンバには `.` でアクセスする。

```cpp
Employee e {};
e.id = 14;
```

## 例

```cpp
#include <iostream>

struct Employee
{
    int id {};
    int age {};
    double wage {};
};

int main()
{
    Employee joe { 14, 32, 60000.0 };
    Employee frank { 15, 28, 45000.0 };

    int totalAge { joe.age + frank.age };
    std::cout << "Joe and Frank have lived " << totalAge << " total years\n";

    if (joe.wage > frank.wage)
        std::cout << "Joe makes more than Frank\n";
    else if (joe.wage < frank.wage)
        std::cout << "Joe makes less than Frank\n";
    else
        std::cout << "Joe and Frank make the same amount\n";
}
```

## 補足

- 単純なデータの集まりを表すときに `struct` がよく使われる
- 振る舞いを強く隠蔽したい設計では `class` が選ばれることが多い
- ただし、これは主に慣習の違いであり、機能差は小さい
- `class` との違いの詳細は [[クラスと構造体の違い（C++）]] を参照

## 関連

- [[クラス（C++）]]
- [[クラスと構造体の違い（C++）]]
- [[集成体]]

## 参考

- https://www.learncpp.com/cpp-tutorial/introduction-to-structs-members-and-member-selection/
- https://www.learncpp.com/cpp-tutorial/struct-aggregate-initialization/
