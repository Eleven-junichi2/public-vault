---
publish: true
tags:
  - CPlusPlus
---
本体を実行したあとで継続条件を判定する[[繰り返し処理]]の構文。
そのため、ループ本体は最低1回は実行される。

```cpp
do
    statement; // 単一の文または複合文（`{}`によるブロック）
while (condition);
```

```cpp
int i{ 0 };
do
{
    std::cout << i << '\n';
    ++i;
}
while (i < 3);
```
