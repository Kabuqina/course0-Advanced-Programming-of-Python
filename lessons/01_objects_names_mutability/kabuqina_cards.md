# Kabuqina Cards · Lesson 01 Objects, Names, Mutability

## Concept Card 1
Q: `is` 和 `==` 有什么区别？
A: `is` 比较身份（是不是同一个对象，`id()` 相同）；`==` 比较值是否相等。判断 None 用 `is None`。

## Concept Card 2
Q: 为什么 `a = b` 之后修改 `b` 会影响 `a`？
A: 赋值不复制对象，只是让两个名字绑定到同一个对象；若该对象可变，任一名字的原地修改都可见。

## Code Card 1
Q: 为什么 `def f(x, acc=[])` 会在多次调用间“记住”之前的数据？
A: 默认值在函数定义时求值一次并被所有调用共享。修复：默认写 None，进函数再新建列表。

## Misconception Card 1
Q: `copy.copy()` 是不是就能得到完全独立的副本？
A: 不是。浅拷贝只复制外层，嵌套的可变子对象仍被共享；需要 `copy.deepcopy()` 才完全独立。

## Tutor Prompt
请像助教一样，对每一行赋值追问：“这一行创建了新对象，还是只是多了一个指向旧对象的名字？”
再让学生用 `id()` 验证判断。
