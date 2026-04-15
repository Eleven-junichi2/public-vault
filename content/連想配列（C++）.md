---
publish: true
tags:
  - CPlusPlus
---

C++では、[[連想配列]]の機能を持つ[[コンテナ（C++）]]が提供されている。

- [[#map]]
- unordered_map

## map

`<map>`ヘッダで提供される、[[二分木]]として実装された[[連想配列]]。

宣言の書式: `std::map<キーの型, 値の型>`

`map`では、各キーは一意であり、同じキーを重複して保持できない。

```cpp
#include <map>
#include <string>

std::map<std::string, int> scores {};
```

```cpp
#include <iostream>
#include <map>
#include <string>

int main()
{
    std::map<std::string, int> scores {};

    scores["Alice"] = 90;
    scores["Bob"] = 75;
    scores.insert({ "Carol", 88 });

    std::cout << scores.at("Alice") << '\n';

    if (scores.contains("Bob")) {
        std::cout << "Bob exists\n";
    }
}
```

- `operator[]`でキーに対応する値へアクセスできる
	- 指定したキーが存在しない場合に、そのキーを持つ要素を新しく作成する
- `at()`は指定したキーの値を取得する
- `insert()`で要素を追加できる
- `find()`や`contains()`でキーの存在を調べられる

## 参考

- https://cpp-lang.sevendays-study.com/ex-day5.html
- https://cpprefjp.github.io/reference/map/map.html
