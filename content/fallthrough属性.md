---
publish: true
tags:
  - CPlusPlus
---
`switch`文で`break`を書かずに次の`case`や`default`へ落ちる直前に`[[fallthrough]];`と書き、意図的な[[フォールスルー]]であることを明示する属性。

```cpp
switch (n) {
case 1:
    std::cout << "one\n";
    [[fallthrough]];
case 2:
    std::cout << "small\n";
    break;
}
```

この例では、`case 1`から`case 2`へ意図的にフォールスルーすることを示している。
