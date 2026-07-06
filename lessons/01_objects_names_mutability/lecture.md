# Lesson 01 讲义 · 对象、名字与可变性

## 1. 名字，不是盒子
Python 里每个值都是一个**对象**，有三样东西：身份（identity，`id()`）、类型（type）、
值（value）。变量是绑定到对象的**名字**。`a = b` 只是让两个名字指向同一对象。

```python
a = [1, 2, 3]
b = a
print(a is b)     # True —— 同一对象
print(id(a) == id(b))  # True
b.append(4)
print(a)          # [1, 2, 3, 4]
```

- `is`：身份比较（同一对象？）
- `==`：值比较（值相等？）
- 经验法则：与 `None` 比较用 `is None`；比较内容用 `==`。

## 2. 可变 vs 不可变
- 不可变（immutable）：`int`、`float`、`str`、`tuple`、`frozenset`——“修改”会产生新对象。
- 可变（mutable）：`list`、`dict`、`set`、多数自定义对象——可原地修改。

```python
s = "abc"
print(id(s))
s += "d"          # 新字符串，id 变化
n = [1]
m = n
m += [2]          # 原地扩展，n 也变成 [1, 2]
```

## 3. 可变默认参数陷阱
默认值在**函数定义时**求值一次，之后所有调用共享它：

```python
def add_grade(grade, scores=[]):     # 只创建一次 []
    scores.append(grade)
    return scores

add_grade(90)   # [90]
add_grade(80)   # [90, 80]  —— 意外共享！
```
修复：
```python
def add_grade(grade, scores=None):
    if scores is None:
        scores = []
    scores.append(grade)
    return scores
```

## 4. 浅拷贝 vs 深拷贝
```python
import copy
shallow = copy.copy(nested)      # 外层新对象，内层仍共享
deep = copy.deepcopy(nested)     # 递归复制，完全独立
```
合并配置、传入可变参数时，若不想污染原始数据，就要 `deepcopy` 或按需新建。

## 5. 作用域：LEGB
名字查找顺序：Local → Enclosing → Global → Built-in。函数内**赋值**会默认创建局部
名字；要改外层变量需 `nonlocal`（闭包）或 `global`（模块级）。这为 Lesson 02 闭包铺垫。

## 6. 常见错误
- 用 `==` 判断“是不是同一个对象”（应用 `is`）。
- 以为 `a = b` 复制了数据。
- 可变默认参数导致跨调用状态泄漏。
- 用 `copy.copy` 处理嵌套结构，却发现内层仍被共享。
