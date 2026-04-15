---
publish: true
tags:
  - CPlusPlus
---
ODR。One Definition Rule。
1つの[[翻訳単位]]の中では、同じ定義可能な項目(definable item)を複数回定義してはならない。
また、複数の[[翻訳単位]]に同じ項目の定義が現れる場合も、それらは一定の条件を満たしていなければならない。

[[内部リンケージ]]を持つ名前は[[翻訳単位]]ごとに別物として扱われるが、その翻訳単位の中で複数定義してよいわけではない。

## 参考

- [[独習C++]] 4.6.2
- https://www.learncpp.com/cpp-tutorial/forward-declarations/
