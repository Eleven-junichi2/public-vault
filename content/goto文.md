---
publish: true
tags:
  - CPlusPlus
---

同じ関数内のラベルへ処理を移す[[文（C++）]]。
通常は[[if文（C++）]]や[[for文]]、[[while文]]などの構造化された制御構文が好まれる。

```cpp
label:
// …
goto label; // 同じ関数内の label へ飛ぶ
```
