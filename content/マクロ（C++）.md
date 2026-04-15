---
publish: true
tags:
  - CPlusPlus
---
マクロは、[[プリプロセッサ（C++）]]が扱う仕組みの1つ。
`#define`などの[[プリプロセッサー命令（C++）]]によって、ソースコードの指定部分(識別子など)を別のコードに置き換えるよう指示できる。マクロは他のファイルのソースコードに影響せず、使っているファイル内のみに影響する。

### 命名規則

- 基本的には[[識別子（C++）#命名規則]]が参考になる
- 大文字で単語の区切りに`_`（アンダースコア）を用いる

### オブジェクト形式マクロ

マクロ識別子を定義することで、ソースコードでそのマクロ識別子を指定すると、プリプロセッサが定義した置換先で置換する。

[[リテラル（C++）]]に名前を付けるような運用ができるが、C++ではより良い方法が用意されているためその使い方は非推奨。

```cpp
#define マクロ識別子 置換先 // 置換先に置換
#define マクロ識別子 // 置換先を省略すると、無に置換。後述する分岐の制御に用いられる
```

#### 例:
```cpp
#include <iostream>

#define MY_NAME "Alex"

int main()
{
    std::cout << "My name is: " << MY_NAME << '\n';
    // プリプロセスで以下に変換される
    // std::cout << "My name is: " << "Alex" << '\n';
    return 0;
}
```

#### 例2:
```cpp
#include <iostream>

void hello()
{
	std::cout << "hello, world" << std::endl;
}

void goodbye()
{
	std::cout << "goodbye, world" << std::endl;
}

int main()
{
	hello();
	
	std::cout << "hello, macro" << std::endl;

#define hello goodbye // 識別子helloをgoodbyeに置換
	
	hello(); // プリプロセッサーによって、コンパイラにはgoodbyeに置換されたものが渡される
	
#undef hello // helloのマクロ定義を消す
	hello() // マクロ定義が消されたので置換されない
}
```

### 関数形式マクロ

関数のような形で引数を受け取り、その引数を使ってコードを置換するマクロ。
ただし、[[関数（C++）]]ではなく、プリプロセッサによる単なる置換である。

標準ライブラリの `assert` も、この種のマクロとして提供される。

```c++
#define macro_name(param1, param2) replacement
```

使用例：
```c++
#define SQUARE(x) ((x) * (x))

int main()
{
	int value{ SQUARE(3) }; // ((3) * (3)) に置換される
}
```

## 関連

- [[条件付きコンパイル]]
- [[assert]]
