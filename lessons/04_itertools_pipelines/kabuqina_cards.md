# Kabuqina Cards · Lesson 04 Itertools and Functional Pipelines

## Concept Card 1
Q: `functools.lru_cache` 解决什么问题？
A: 缓存纯函数的结果，避免重复计算；适合递归或昂贵的查询函数。要求参数可哈希。

## Concept Card 2
Q: `functools.singledispatch` 和一长串 `if/elif isinstance(...)` 相比有什么优势？
A: 把类型判断和对应实现拆开，新增类型只需再注册一个函数，更易扩展和阅读。

## Code Card 1
Q: 为什么 `itertools.groupby` 通常要先 `sorted`？
A: `groupby` 只合并**连续相同**的 key；不排序会把分散的相同 key 分成多组。

## Misconception Card 1
Q: itertools 是不是永远比 list 更快？
A: 不一定。它的主要优势是惰性和省内存；数据量小或需要随机访问时，list 可能更简单、更快。

## Tutor Prompt
请像助教一样，先给学生一段用 `if isinstance(x, int): ... elif isinstance(x, str): ...` 实现的代码，
让他把它改写成 `singledispatch` 版本，并解释为什么新增类型时更方便。
