---
publish: true
tags:
  - CPlusPlus
---
明示的に指示する型変換。
主に、数値型の変換や関連する型どうしの変換に用いられる。

```cpp
static_cast<変換先の型>(変換する値)
```

```cpp
double x { 3.8 };
int n { static_cast<int>(x) };
```
