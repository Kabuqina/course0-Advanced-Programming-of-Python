# Kabuqina Cards · Lesson 05 Decorators

## Concept Card 1
Q: `@deco` 到底做了什么？
A: 它是语法糖，等价于 `func = deco(func)`：用装饰器返回的新函数替换原函数名字。

## Concept Card 2
Q: 带参数的装饰器为什么需要三层函数？
A: 最外层吃装饰器参数并返回装饰器，中层吃被装饰函数并返回 wrapper，wrapper 吃真正的调用参数。

## Code Card 1
Q: 不用 `functools.wraps` 会有什么后果？
A: wrapper 会顶替原函数的 `__name__`/`__doc__`/签名，调试、文档和自省都会看到 “wrapper”，信息失真。

## Misconception Card 1
Q: 装饰器是不是会改变被装饰函数的源代码？
A: 不会。它只是用一个包装函数替换名字绑定，原函数对象本身不变。

## Tutor Prompt
请像助教一样，把 `@timed` `@repeat(3)` 两层装饰器画成“盒中盒”，
并让学生说出 `roll = timed(repeat(3)(roll))` 的组合顺序。
