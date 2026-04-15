---
publish: true
tags:
  - CMake
---
`compile_commands.json` の出力を有効化する[[変数]]。

`CMAKE_EXPORT_COMPILE_COMMANDS` を `ON` にすると、生成時にビルドディレクトリへ `compile_commands.json` が出力される。  
このファイルには、各ソースファイルを実際にどのコンパイラ・オプション・インクルードパスでコンパイルするかが記録される。

例:
```cmake
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
```

## 用途

- `clangd` などの LSP が正しい補完や定義ジャンプを行うために使う
- `clang-tidy` などの静的解析ツールが実際のコンパイル設定を参照するために使う
- どのコンパイルオプションやインクルードパスが適用されているかを確認する

## 参考

- [CMAKE_EXPORT_COMPILE_COMMANDS — CMake Documentation](https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html)
