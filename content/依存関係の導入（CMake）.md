---
publish: true
tags:
  - CMake
---
CMakeでは、依存関係となるライブラリ等を利用する場合、[[ターゲット（CMake）|ターゲット]]として取りこみ[[target_link_librariesコマンド]] でリンクする。

## プロジェクト配下で管理し導入する場合

同じプロジェクト下に依存関係を配置する場合は、自分のプロジェクト側で[[add_libraryコマンド]]などを用いてライブラリの[[ターゲット（CMake）|ターゲット]]を定義し、リンクして利用できる。

ライブラリを[[サブディレクトリ（CMake）]]で扱う場合は、[[add_subdirectoryコマンド]]で取り込んでその中で定義されたライブラリの[[ターゲット（CMake）|ターゲット]]をリンクして利用できる。

## システムやパッケージマネージャで管理し導入する場合

システムやパッケージマネージャで導入したライブラリは、[[find_packageコマンド]]により[[パッケージ（CMake）]]として導入できる場合があり、その[[インポートターゲット（CMake）]]をライブラリの[[ターゲット（CMake）]]としてリンクして利用できる。

## 関連

- [[target_link_librariesコマンド]]
- [[ターゲット（CMake）]]
- [[CMakeLists.txt]]
- [[外部ライブラリの導入と管理]]
- [[SDLの導入]]

## 参考

- https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html
- https://cmake.org/cmake/help/latest/guide/tutorial/Finding%20Dependencies.html
