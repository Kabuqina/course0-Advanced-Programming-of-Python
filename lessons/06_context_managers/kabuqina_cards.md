# Kabuqina Cards · Lesson 06 Context Managers

## Concept Card 1
Q: `with` 相比手写 `try/finally` 好在哪？
A: 它把“获取 + 释放”封装成一个可复用对象，调用处更简洁，且释放逻辑不会被遗忘。

## Concept Card 2
Q: `__exit__` 返回 True 和 False 有什么区别？
A: 返回 True 表示异常已被处理、不再向外传播（吞掉异常）；返回 False（或 None）则让异常继续抛出。

## Code Card 1
Q: 用 `@contextlib.contextmanager` 时，yield 前后分别对应什么？
A: yield 之前相当于 `__enter__`，yield（放在 try 里）之后的 finally 相当于 `__exit__` 的清理。

## Misconception Card 1
Q: 原子写为什么要先写临时文件再替换？
A: 避免写到一半程序崩溃，留下一个损坏的目标文件；`os.replace` 是原子操作，要么旧要么新。

## Tutor Prompt
请像助教一样，让学生在 with 块里故意抛异常，观察 `__exit__` 是否仍被调用，
再解释为什么资源清理必须放在 finally。
