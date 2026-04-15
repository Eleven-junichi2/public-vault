---
publish: true
tags:
  - CPlusPlus
---
RTTI。

run-time type information。  
実行時に[[オブジェクト（C++）]]の型に関する情報を扱う仕組み。
RTTIを使うと、プログラムの実行中に、あるオブジェクトが実際にはどの型であるかを調べられる。



## dynamic_castとの関係

[[dynamic_cast]]は、基底クラスへのポインタや参照が実際にはどの派生クラスを指しているかを、実行時に検査している。  
この検査に必要なのがRTTIである。

そのため、RTTIが無効化されている環境では、[[dynamic_cast]]は正しく動作しない。

## 注意

- RTTIには追加の空間コストや実行時コストがかかることがある
- そのため、処理系によっては最適化のためにRTTIを無効化できる場合がある
- ただし、RTTIに依存するコードでは、そのような設定に注意が必要である

## 関連

- [[dynamic_cast]]
- [[ダウンキャスト]]

## 参考

- https://www.learncpp.com/cpp-tutorial/dynamic-casting/
