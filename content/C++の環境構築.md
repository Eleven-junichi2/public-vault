---
publish: true
tags:
  - CPlusPlus
---
C++の開発環境を構築するには、まず[[コンパイラ]]を用意する。  
必要に応じて[[1_Archives/CMake]]などのビルドツールや、[[Visual Studio Code]]などのエディタを導入する。

## macOS

- Xcode Command Line Tools または Xcode を導入すると、`clang++` が使える
- 必要に応じて [[1_Archives/CMake]] を導入する

## Windows

代表的な選択肢は次の2つ。

- MSVC を使う
- MSYS2 を導入し、MinGW-w64 の `g++` を使う

## 参考

- https://developer.apple.com/xcode/resources/
- https://www.msys2.org/
- https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation
- https://code.visualstudio.com/docs/cpp/config-mingw
