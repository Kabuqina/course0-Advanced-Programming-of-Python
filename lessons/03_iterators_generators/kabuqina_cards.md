# Kabuqina Cards · Lesson 03 Iterators and Generators

## Concept Card 1
Q: iterable 和 iterator 的区别是什么？
A: iterable 是“可以被迭代”的对象（实现 `__iter__`）；iterator 是“正在执行迭代过程”的对象，实现 `__next__` 并保存进度。

## Code Card 1
Q: 这段生成器函数为什么不会立刻读取文件？
A: 因为调用生成器函数只返回 generator 对象，函数体要到 `next()` 或 `for` 才逐步执行。

## Misconception Card 1
Q: 生成器是不是永远比 list 更快？
A: 不一定。生成器的优势是惰性和低内存；数据很小时 list 可能更简单甚至更快。

## Misconception Card 2
Q: 为什么一个生成器 `for` 遍历完再遍历一次就空了？
A: 生成器只能消费一次，进度耗尽后不再产出。需要多次遍历就存成 list 或重新创建生成器。

## Tutor Prompt
请像助教一样，先让学生猜 `list(read_ints(path))` 与直接 `for` 迭代在内存上的差别，
再让他解释 for 循环如何调用 `iter()` 与 `next()`。
