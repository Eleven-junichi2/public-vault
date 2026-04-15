---
publish: true
tags:
  - CPlusPlus
---
`static`キーワード。
宣言される場所により意味が変わる。

- [[名前空間（C++）]]の[[スコープ（C++）]]にある[[変数（C++）]]や[[関数（C++）]]に付けると、主に[[内部リンケージ]]を与える[^internal_linkage]
- ブロック内の変数に付けると、[[静的ローカル変数]]になる[^static_block_var]
- [[クラス（C++）]]のメンバに付けると、特定の[[インスタンス（C++）]]ではなくクラス全体に属するメンバになる（[[静的メンバ変数]]・[[静的メンバ関数]]）[^static_storage_duration]

## 参考

- https://en.cppreference.com/w/cpp/language/storage_duration.html
- https://en.cppreference.com/w/cpp/language/static.html

[^static_storage_duration]: https://en.cppreference.com/w/cpp/language/storage_duration.html#Static_storage_duration
[^internal_linkage]: https://en.cppreference.com/w/cpp/language/storage_duration.html#Internal_linkage
[^static_block_var]: https://en.cppreference.com/w/cpp/language/storage_duration.html#Static_block_variables
