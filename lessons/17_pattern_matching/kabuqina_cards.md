# Kabuqina Cards · Lesson 17 Pattern Matching

## Concept Card 1
Q: `match/case` 和一串 `if/elif` 的关键区别是什么？
A: match/case 按**结构**匹配，命中分支的同时把子字段解构到变量；if/elif 只做布尔判断。

## Concept Card 2
Q: 映射模式 `{"type": "click", "x": x}` 是否要求字典只有这些键？
A: 不要求。它只要求字典至少包含这些键，多余键不影响匹配。

## Code Card 1
Q: 为什么 `case RED:` 可能不按预期工作？
A: case 里的裸变量名是**捕获变量**，不是与外部变量比较。要比较常量得写字面量或枚举属性。

## Misconception Card 1
Q: 用了 `match/case`，Python 就变成静态类型语言了吗？
A: 没有。模式匹配只是新的控制流工具，类型仍是动态的；`case int(x)` 里的 `int` 只是模式 guard，不是类型声明。

## Tutor Prompt
请像助教一样，先给学生一段用多个 `if event.get("type") == "click": ... elif ...` 写的代码，
让他改写成 `match/case`，然后问他：如果字典里还多了一个 `"timestamp"` 字段，匹配结果会变吗？为什么？
