---
publish: true
tags:
  - IT
---
プログラムの観測可能な動作（observable behavior）が変わらない限り、処理系はプログラムをそのように実行したかのように振る舞えばよい、という規則。
観測可能な動作には、入出力や `volatile` オブジェクトへのアクセスなどが含まれる。

この規則により、処理系は命令の並べ替えや不要な計算の削除、[[コンパイル時評価]]などを行える。

## 参考

- https://eel.is/c++draft/intro.execution
- https://docs.oracle.com/cd/E19957-01/805-7885/z40000214bee/index.html
- https://www.learncpp.com/cpp-tutorial/the-as-if-rule-and-compile-time-optimization/
- https://www.learncpp.com/cpp-tutorial/constant-expressions/
