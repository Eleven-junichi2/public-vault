---
publish: true
tags:
  - CPlusPlus
---
呼び出すことで処理を実行し、必要に応じて値を返すもの。

```cpp
returnType functionName(parameters) // 関数ヘッダー（function header）
{
	// function body
}
```

## 関数パラメータ・引数

関数ヘッダーには、呼び出し元が[[引数]]を渡す先となる、関数内で扱える変数であるパラメータを設定できる：`functionName(,で区切られたパラメータのリスト)`

## 注意

返り値の型が`void`以外の関数で`return`文を実行しないまま終了すると、[[未定義動作]]になる。

## main関数

C++では、`main関数`が[[エントリポイント]]となる。
返り値の型は`int`で、[[ステータスコード]]を表す

```cpp
int main()
{
	// …
	return 0; // main関数では省略可能
}
```
