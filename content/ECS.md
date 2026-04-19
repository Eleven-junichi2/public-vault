---
tags:
  - GameDev
publish: true
---
Entity Component System。ゲーム開発で用いられる、ソフトウェア設計のパラダイムであり、[[コンポジション]]に基づいて設計をする。

エンティティ（**Entity**）は、ゲーム内のあらゆるオブジェクトを、Componentの組み合わせで一意に表現する単位である。1つのEntityは、同じ種類のComponentを複数持たない。
コンポーネント（**Component**）は、基本的には処理を持たない、Entityに付随する**純粋なデータ**である。
システム（**System**）は、EntityとそのComponentから振る舞いを定義する。

> 例: Player entityは、ComponentとしてPos, Speed, BBox, Sprite, Health, Gravity, Inputを持つ。Tile entityは、Pos, BBox, Spriteを持つ。Movement Systemは全てのentityを走査し、各エンティティの座標を表すPos componentの値にSpeed componentの値を加える。

## ゲームエンジン設計の例

- GameEngine
	- Scene: 論理的に異なるゲームの場面を管理する。
		- Systems
		- EntityManager: Entityの生成と管理を行う
			- Entity
				- Component

## コンポーネントの格納の実装パターン

### 1. 各コンポーネントをメンバ変数として直接保持するパターン

C++での例:
```cpp
class Entity {
    CTransform cTransform;
    CName      cName;
    CShape     cShape;
    // すべての可能なコンポーネントを列挙
};
```
- **利点**
    - 実装が最も単純で理解しやすい。
    - メモリが連続的（Contiguous Memory）に配置されるため、キャッシュ効率が良い。
    - ヒープ（new/delete）を使用しないため高速。
- **欠点**
    - コンポーネントの動的な追加・削除ができない。
    - コンポーネントが「有効かどうか」を調べられるように、各コンポーネントがそれを示すフラグ（例：`bool exists`）を持つ必要がある。
    - クラスの内部構造を知っている必要があり、カプセル化が不十分。

### 2. 各コンポーネントを生ポインタ（Raw Pointers）で使用するパターン

C++での例:
```cpp
class Entity {
    CTransform * cTransform = nullptr;
    CName      * cName      = nullptr;
    // ...
};
```
- **利点**
    - ポインタが `nullptr` かどうかで、コンポーネントが存在するかを判定できる。 
- **欠点**
    - メモリ管理（new/delete）を手動で行う必要があり、メモリリークのリスクが高い。 
    - コンポーネントの入れ替え時に、古いメモリを解放し忘れる危険がある。
    - ヒープ利用によるオーバーヘッドがあり、実行速度が低下する。

### 3. スマートポインタを使用するパターン

C++での例:
```cpp
class Entity {
    std::shared_ptr<CTransform> cTransform;
    std::shared_ptr<CName>      cName;
    // ...
};
```
- **利点**
    - RAIIに基づき、メモリ管理が自動化され安全になる（メモリリークの防止）。
    - `nullptr` チェックによって存在確認が可能。
- **欠点**
    - `shared_ptr` 自体のオーバーヘッドが大きく、パフォーマンスが非常に低下する。 
    - ヒープを使用するため、メモリの連続性が失われキャッシュ効率が悪くなる。
    - 構文が冗長（`std::make_shared` など）になりがち。

### 4.  可変長配列で管理するパターン

C++での例:
```cpp
class Entity {
    std::vector<Component*> components;
public:
    Entity() {}
    void add<T>(args);
    T& get<T>(); // T型のコンポーネントを取得
    bool has<T>(); // T型のコンポーネントを持つか調べる
    void remove<T>(); // T型のコンポーネントを削除する
};
```

```cpp
e.add<CTransform>(Vec2(100, 200));
e.add<CName>("Red Box");
e.add<CShape>(args);
if (e.has<CTransform>())
{
// …
}
```
- **利点**
    - ストレージの詳細が抽象化されている。
    - ストレージの変更（ベクトルから別の構造へ）が、ゲームロジック側のコードに影響を与えない。
- **欠点**
    - 特定の型（コンポーネント）を取り出す際に `dynamic_cast` 等が必要になり、実行速度が遅い。 
    - C++では型情報の動的な扱いが難しいため、型の判定や取得の実装が複雑になる。 

### 5. タプルを使用するパターン（推奨）

C++での例:
```cpp
class Entity
{
    std::tuple<C1, C2, C3, C4> m_components;
public:
    Entity() {}
    void add<T>(args);
    T& get<T>;
    bool has<T>();
    void remove<T>();
};
```

```cpp
Entity e;
e.add<CTransform>(Vec2(100, 200));
e.add<CName>("Red Box");
e.add<CShape>(args);
if (e.has<Transform>())
{
// …
}
```
- **利点**
    - コンパイル時に型が確定するため、アクセスが非常に高速（定数時間）。
    - 抽象化されており、`get<T>()` や `has<T>()` といったクリーンなAPIを提供できる。 
    - 異なる型のComponentを1つのEntity内にまとめて保持できるため、個別にヒープ確保する場合に比べて、メモリ効率や局所性の面で有利になりやすい。
- **欠点**
    - タプルに含めるすべてのコンポーネント型を事前に定義しておく必要がある
    - C++では実装にテンプレートメタプログラミングの知識が多少必要。 

全てのコンポーネント型を含めるタプル型は、エイリアスを定義して扱うのが便利（C++での例）:
```cpp
using ComponentTuple = std::tuple<
    CTransform,
    CLifeSpan,
    CInput,
    CBoundingBox,
    CAnimation,
    CGravity,
    CState
>;
```

## Entityの実装パターン

- 識別のために、一意のID（整数）を持つ。
- 自身が現在有効かを示すフラグ（真偽値）を持つ。
- グループや種類分けのためのタグ（文字列または整数など）を持つ。

C++での例:
```cpp
class Entity
{
    ComponentTuple m_components;
    bool m_alive {true};
    std::string m_tag {"default"};
    size_t m_id {0};
public:
    Entity() = default;

    template <typename T, typename... TArgs>
    T& add(TArgs&&... args);

    template <typename T>
    T& get();

    template <typename T>
    const T& get() const;

    template <typename T>
    bool has() const;

    template <typename T>
    void remove();

    size_t id() const;
    bool isAlive() const;
    void destroy();
    const std::string& tag() const;
};
```

## Componentの実装

- ロジックを含まず、純粋なデータのみを保持する
- Entityに保持されているかを示すフラグを持つ

C++での例:
```cpp
// Componentの基底クラス
class Component
{
public:
    bool exists {false}; // Entityに保持されているかを示すフラグ
};

class CTransform : public Component
{
public:
    Vec2 pos {0, 0};
    Vec2 velocity {0, 0};
    CTransform() {}
    CTransform(const Vec2& p, const Vec2& v)
        : pos(p), velocity(v) {}
};
```

## Systemの実装パターン

- 各エンティティを操作する
- システムの対象を特定のコンポーネント（の組み合わせ）を持つエンティティのみに指定して実装できる。

C++での例:
```cpp
void sRender()
{
    for (auto& e : m_entityManager.getEntities())
    {
        if (e.has<CShape>() && e.has<CTransform>())
        {
            auto& shape = e.get<CShape>();
            auto& transform = e.get<CTransform>(); // transformのposの型はメンバxとメンバyを持つとする

            shape.shape.setPosition(transform.pos.x, transform.pos.y);
            window.draw(shape.shape);
        }
    }
}
```

## Entity Managerの実装パターン

- [[Factoryデザインパターン]]を採用し、Entityを扱う。
	- 全てのEntityの作成
	- 全てのEntityの格納
	- 全てのEntityの生存（期間）管理
	- Entity Managerを介することで、[[イテレータの無効化]]のような問題をエンティティの利用者から切り離しやすくなる

### Entityの格納方法の実装パターン

1. エンティティを直接配列に格納する
	- 利点:
		- [[スマートポインタ]]の[[オーバーヘッド]]を避けられる
		- メモリに連続的に配置されるため、キャッシュ効率が良い
		- 設計がシンプルになる
	- 欠点:
		- 格納するエンティティの所有権や参照、生存期間がそれらを格納するコンテナに縛られる
		- エンティティの削除は遅い
		- [[イテレータの無効化]]の問題が発生する

2. エンティティのスマートポインタを配列に格納する
	- 利点:
		- 所有権の共有により、安全に複数のシステムで生存期間の心配をせずにエンティティを複数のシステムで参照できる
		- 自動メモリ管理
		- エンティティの追加と削除が比較的早い（データ量が比較的少ない）
		- 他の場所でエンティティを参照し続けながら、そのエンティティを格納する
		- 配列を修正できる
	- 欠点:
		- [[スマートポインタ]]の[[オーバーヘッド]]
		- エンティティがメモリへ連続的に配置されない
3. エンティティを整数インデックスで管理するメモリプールでエンティティのデータを格納する

- 全てのエンティティを保持する[[配列]]と、タグごとに配列を分類する[[連想配列]]を併用することで、特定の種類のエンティティだけを高速に取得することができる

### C++での例

```cpp
using EntityVec = std::vector<std::shared_ptr<Entity>>;
using EntityMap = std::map<std::string, EntityVec>;

class EntityManager
{
    EntityVec m_entities;
    EntityVec m_toAdd; // 追加したいエンティティを保持するバッファ
    EntityMap m_entityMap;
    size_t m_totalEntitites = 0; // 作成されたEntityの総数
public:
	EntityManager();
	void update();
	std::shared_ptr<Entity> addEntity(const std::string& tag);
	EntityVec& getEntites()
	EntityVec& getEntites(const std::string& tag)
}
```

#### イテレーターの無効化への対策

[[イテレータの無効化#対策|遅延効果]]による対策を実装するために、追加・削除したいエンティティを保持する[[バッファ]]としての配列を用意する。

```cpp
std::shared_ptr<Entity> EntityManager::addEntity(tag)
{
    auto e = std::make_shared<Entity>(tag, m_totalEntities++);
    m_toAdd.push_back(e);
    return e;
}
```

`update()`メンバ関数によって、次のフレームで実際にバッファから反映される実装:
```cpp
void EntityManager::update()
{
	for (auto e : m_toAdd)
	{
	   m_entities.push_back(e);  
	   m_entityMap[e->tag()].push_back(e);
	}
	for (auto e : m_entities)
	{
		// if e is dead, remove it from m_entities
		// if e is dead, remove it from m_entityMap[e->tag()]
		// AIへ ここでのイテレータの無効化を解決するように、このコードブロック全体を修正してください
	}
	m_toAdd.clear()
}
```

## 関連

- [[スマートポインタ]]

## 参考

- [COMP4300 - Game Programming - Lecture 04 - Intro to ECS in C++ (Entities, Components, Systems)](https://www.youtube.com/watch?v=8_DeUkjQcSU)
