---
publish: true
tags:
  - CPlusPlus
---
C++の`class`。
`class` は [[クラス型（C++）]] を定義するためのキーワード。
`class` と `struct` で定義される型はどちらも[[クラス型（C++）]]であり、`class` ではメンバと基底クラスのデフォルトの[[アクセス指定子]]が `private` になる。

[[クラス型（C++）]]は、データとそれを操作する関数をひとまとめにできる[[ユーザー定義型]]である。

## 定義の書式

```cpp
class ClassName : access-specifier BaseName
{
private:
    // データメンバ

protected:
    // 派生クラスから使うメンバ

public:
    // コンストラクタ
    // メンバ関数
};
```

継承しない場合は `: access-specifier BaseName` を省略できる。
`private:`、`protected:`、`public:` は必要に応じて配置する。
クラス定義は宣言の一種であるため、定義の末尾には `;` が必要である。

## オブジェクトの作成

`class` で定義した型のオブジェクトも、ほかの[[クラス型（C++）]]と同じく、選んだ初期化形式に従って初期化される。

## `struct` との違い

[[クラスと構造体の違い（C++）]] を参照。

## 例

```cpp
class Battery
{
private:
    float energy_ {};

public:
    Battery(float energy)
        : energy_ { energy }
    {
    }

    float energy() const
    {
        return energy_;
    }
};

int main()
{
    Battery pack { 0.9f };
    float remaining { pack.energy() };
}
```

## 関連

- [[構造体（C++）]]
- [[クラスと構造体の違い（C++）]]
- [[クラス型（C++）]]
- [[メンバ関数]]
- [[アクセス指定子]]

## 参考

- https://learn.microsoft.com/ja-jp/cpp/cpp/classes-and-structs-cpp?view=msvc-170
- https://learn.microsoft.com/ja-jp/cpp/cpp/cpp-type-system-modern-cpp?view=msvc-170#user-defined-types
- https://www.learncpp.com/cpp-tutorial/introduction-to-classes/
