---
publish: true
tags:
  - CMake
---
CMakeでは、依存関係となるライブラリを利用する場合、ライブラリを[[add_libraryコマンド]]によって[[ターゲット（CMake）|ターゲット]]として定義し、その[[ターゲット（CMake）]]を[[target_link_librariesコマンド]] で指定することでビルド時にリンクするように設定できる。

いずれかの方法で、自動化された（またはこちらで自動化した）方法で簡潔にライブラリのターゲット定義を行える。
1. ライブラリのディレクトリに、そのライブラリのターゲット定義を行う[[CMakeLists.txt]]が用意されている（またはこちら側で作成する）場合は、ライブラリのディレクトリを[[サブディレクトリ（CMake）]]としてプロジェクトのディレクトリ下に直接置き、[[add_subdirectoryコマンド]]によって処理することで、利用したいライブラリのターゲット定義を導入する
2. 取り込むターゲット（[[インポートターゲット（CMake）]]）の定義を自動化する[[find_packageコマンド]]用のスクリプトが用意されている場合は、それを指定することで、利用したいライブラリのターゲット定義を導入する
	- [[find_packageコマンド]]では、ライブラリがシステムに導入される場所を探索するため、

## システムやパッケージマネージャで導入したものを利用する場合

ライブラリがCMakeに対応している場合、前述の **2.** の方法を利用できる。

## 関連

- [[target_link_librariesコマンド]]
- [[ターゲット（CMake）]]
- [[CMakeLists.txt]]
- [[外部ライブラリの導入と管理]]
- [[SDLの導入]]

## 参考

- https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html
- https://cmake.org/cmake/help/latest/guide/tutorial/Finding%20Dependencies.html
- https://theolizer.com/cpp-school3/cpp-school3-10/