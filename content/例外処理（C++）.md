---
publish: true
tags:
  - CPlusPlus
---
例外処理とは、プログラム実行中にエラーが発生したときに通常の処理を中断し、エラー発生時用の処理へ制御を移すための仕組み。

- `throw`
  - 例外を送出する
- `try`ブロック
  - 例外が起きる可能性のある処理を囲む
- `catch`ブロック
  - 送出された例外を受け取って処理する

## 基本

```cpp
try
{
    throw -1;
}
catch (int x)
{
    std::cerr << "error: " << x << '\n';
}
```

この例では、`throw -1;` によって `int` 型の例外が送出され、対応する `catch (int x)` がそれを受け取る。

`throw` が実行されると、その時点で通常の実行は中断され、対応する `catch` ブロックへ制御が移る。

```cpp
try
{
    throw 4.5;
    std::cout << "This never prints\n";
}
catch (double x)
{
    std::cerr << x << '\n';
}
```

この例では、`throw 4.5;` の後ろの文は実行されない。

`catch` は、送出された例外の型に一致するものが選ばれる。

```cpp
try
{
    throw -1;
}
catch (double)
{
}
catch (int x)
{
    std::cerr << x << '\n';
}
```

この場合、`int` 型の例外は `catch (int x)` で処理される。  
例外の型一致では、通常の関数呼び出しのような暗黙変換は基本的に行われない。たとえば、`int` 型の例外は `catch (double)` では受け取れない。

## クラス型の例外

クラス型の例外は、通常 `const` 参照で受け取る。

```cpp
catch (const std::string& exception)
{
    std::cerr << exception << '\n';
}
```

これは不要なコピーを避けるためであり、場合によっては [[オブジェクトスライシング]] を防ぐ意味もある。

## catchでよく行うこと

- エラーメッセージを表示する
- 呼び出し元へエラーを返す
- 別の例外を再送出する
- `main()` で致命的なエラーを受けて終了処理する

## 関数とスタック巻き戻し

例外は、例外を送出した関数自身で処理しなくてもよい。呼び出し先の関数で `throw` された例外を、呼び出し元の `try`-`catch` で処理できる。

```cpp
#include <cmath>
#include <iostream>

double mySqrt(double x)
{
    if (x < 0.0)
        throw "Can not take sqrt of negative number";

    return std::sqrt(x);
}

int main()
{
    try
    {
        double d{ mySqrt(-4.0) };
        std::cout << d << '\n';
    }
    catch (const char* exception)
    {
        std::cerr << exception << '\n';
    }
}
```

このように、例外はコールスタックをさかのぼって、処理できる `catch` を探す。

この過程で、現在の関数から呼び出し元へ戻るためにコールスタックを巻き戻すことを stack unwinding（スタック巻き戻し）という。

スタック巻き戻しが起こると、巻き戻される関数のローカル変数は通常どおり破棄される。  
そのため、自動変数の [[デストラクタ（C++）]] は例外時にも呼ばれる。

処理できる `catch` が見つかったら、実行はその `catch` ブロックへ移り、処理後はその後ろから再開される。

## キャッチされなかった例外

どの `catch` にも一致しない例外は未捕捉例外となり、最終的に `std::terminate()` が呼ばれてプログラムが終了する。

このとき、コールスタックが必ず巻き戻される保証はない。  
そのため、[[関数（C++）]] の [[ローカル変数（C++）]] が破棄されず、[[デストラクタ（C++）]] を通じたクリーンアップ処理が行われない可能性がある。

実装によっては、未捕捉例外発生時点の情報を保ってデバッグしやすくするために、スタックを十分に巻き戻さず `std::terminate()` に移ることがある。

つまり、未捕捉例外が起きたときは「通常の後始末が走ることを前提にしてはいけない」。

## catch-all handler

`catch (...)` は、型に関係なく任意の例外を受け取る catch-all handler。

```cpp
#include <iostream>

int main()
{
    try
    {
        throw 5;
    }
    catch (double x)
    {
        std::cout << "We caught an exception of type double: " << x << '\n';
    }
    catch (...)
    {
        std::cout << "We caught an exception of an undetermined type\n";
    }
}
```

この例では、`int` 型の例外に一致する具体的な `catch` がないため、最後の `catch (...)` が選ばれる。

`catch (...)` はどんな例外にも一致してしまうため、具体的な `catch` より後ろ、つまり catch 連鎖の最後に置く必要がある。

空の `catch (...) {}` も書けるが、これは「予期しない例外で即座に未捕捉例外扱いになるのを防ぐための最低限の受け口」であって、積極的なエラー回復ではない。

## `main()` での利用

`main()` 全体を catch-all handler で囲んで、予期しない例外が外へ漏れたときに最低限の終了処理を行うことがある。

```cpp
#include <exception>
#include <iostream>

int runApplication()
{
    throw "unexpected failure";
}

int main()
{
    try
    {
        return runApplication();
    }
    catch (const std::exception& exception)
    {
        std::cerr << "Fatal error: " << exception.what() << '\n';
    }
    catch (...)
    {
        std::cerr << "Fatal error: an unexpected exception occurred\n";
        // ここでログ保存やセッション保存など、最小限の後始末を行うことがある
    }

    return 1;
}
```

この用途では、異常終了メッセージを出したり、ログやセッション情報を保存したりしてから終了する。

ただし、catch-all handler に到達した時点でプログラム状態は信頼できない可能性がある。  
そのため、ここでの目的は「回復して続行すること」ではなく、「最低限の cleanup をして安全に終了すること」になる。

## デバッグ時の注意

catch-all handler があると、本来は未捕捉例外としてデバッガが止められたはずの例外が `catch (...)` に吸収され、原因追跡がしにくくなることがある。

そのため、デバッグビルドでは catch-all handler を無効化し、リリースビルドでのみ有効にすることがある。

```cpp
int main()
{
    try
    {
        return runApplication();
    }
#ifndef NDEBUG
    catch (const DummyException&)
    {
    }
#else
    catch (...)
    {
        std::cerr << "Fatal error\n";
    }
#endif
}
```

`DummyException` を使った `catch` は、構文上 `try` に対応する `catch` を残しつつ、実際には通常発生しない例外しか捕まえないようにするためのダミー。

デバッグ中は例外をそのまま外へ出して未捕捉例外として止め、リリース時だけ catch-all handler で最終防衛線を置く、という使い分けができる。

## 参考

- https://www.learncpp.com/cpp-tutorial/basic-exception-handling/
- https://www.learncpp.com/cpp-tutorial/exceptions-functions-and-stack-unwinding/
- https://www.learncpp.com/cpp-tutorial/uncaught-exceptions-catch-all-handlers/
- https://rinatz.github.io/cpp-book/ch10-01-exceptions/
