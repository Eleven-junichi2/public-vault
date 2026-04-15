---
publish: true
tags:
  - CPlusPlus
---
初期化、継続条件、更新を1か所にまとめて書ける[[繰り返し処理]]の構文。

```cpp
for (初期化文; 継続条件; 各周終了時の式) // 各部分は省略可能
    文;
```

次の[[while文]]とほぼ同じ：
```cpp
{
    初期化文;
    while (継続条件)
    {
        文;
        各周終了時の式;
    }
}
```

カウンタ変数を使った繰り返しでよく用いられる。

## 例

```cpp
for (int i {0}; i < 10; ++i)
{
    std::cout << i << '\n';
}
```

### 初期化文を省略

```cpp
int i {0};
for (; i < 10; ++i)
{
    std::cout << i << '\n';
}
```

## 参考

- https://www.learncpp.com/cpp-tutorial/for-statements/
