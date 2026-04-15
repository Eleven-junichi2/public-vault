---
publish: true
tags:
  - CPlusPlus
---
namespace。名前を所属させるための、名前の付いた[[宣言領域（C++）]]。
その結果として、同じ名前でも異なる名前空間に属させることで[[名前の衝突（C++）]]を避けられる。

## 宣言

`namespace`キーワードを用いる。

```c++
// 名前空間の指定
namespace namespace-name
{
	namespace-body…
	// ネスト可能
	// ネストの省略記法：
	    /* namespace toplevel-name::nested-name::…
		   {
			   …
		   }
	    */
}
```

同じ名前空間の宣言を複数箇所で行うことはできる。

### 命名規則

歴史的には、標準ライブラリのように小文字が一般的だったが、現代では、それらやライブラリとの衝突を避けるために、大文字で始める命名規則も推奨され始めている。どちらでもよい。

## 名前空間へのアクセス

トップレベルで宣言された名前は、[[グローバル名前空間（C++）]]に属する。
ある名前空間の名前を明示して使う時は、[[スコープ解決演算子]]によって所属する名前空間を指定する。

## namespaceの別名

```c++
namespace new-namespace-name = old-namespace-name;
```

## 関連

- [[using指令（C++）]]

## 参考

- https://learn.microsoft.com/ja-jp/cpp/cpp/namespaces-cpp?view=msvc-170
- https://www.learncpp.com/cpp-tutorial/user-defined-namespaces-and-the-scope-resolution-operator/
