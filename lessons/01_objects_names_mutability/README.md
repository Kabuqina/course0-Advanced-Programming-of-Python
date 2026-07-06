# Lesson 01 · 对象、名字与可变性

## 目标
- 理解 Python 的“变量”是**名字绑定到对象**，不是盒子。
- 区分 `is` / `==`、`id()` / 值、mutable / immutable。
- 理解并修复**可变默认参数**陷阱。
- 用浅拷贝 / 深拷贝避免共享可变状态“坑人”。

## 要点

赋值 `a = b` 不复制对象，只是让 `a` 与 `b` 指向**同一个对象**。`is` 比较身份
（是不是同一个对象，`id()` 相同），`==` 比较值。

```python
a = [1, 2, 3]
b = a            # 同一个 list
b.append(4)
print(a)         # [1, 2, 3, 4] —— a 也变了
```

**可变默认参数**只在函数定义时创建一次，会在多次调用间被共享：

```python
def add_grade(grade, scores=[]):   # 陷阱！
    scores.append(grade)
    return scores
```

修复方式：默认用 `None`，进函数再新建。

## 本课练习（见 `exercises.py`）
1. `add_grade(grade, scores=None)`：修复可变默认参数 bug。
2. `safe_update_config(base, patch)`：合并配置且不污染 `base`（含嵌套）。
3. `independent_copy(data)`：返回与原对象相等但完全独立的深拷贝。

运行示例：`python lessons/01_objects_names_mutability/examples.py`
做完练习后：`pytest tests/test_01_objects_names_mutability.py`
