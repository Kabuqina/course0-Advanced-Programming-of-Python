# 模块 1 · 迭代器与生成器

## 目标
- 理解**可迭代对象**与**迭代器**的区别及迭代协议
- 用**生成器**实现惰性求值，处理大/流式数据而不占用大量内存
- 掌握 `yield from`、生成器管道（pipeline）与聚合

## 要点

**迭代协议**：可迭代对象实现 `__iter__` 返回一个迭代器；迭代器实现 `__next__`，
在没有更多元素时抛出 `StopIteration`。`for` 循环、解包、`list()` 都建立在此之上。

**生成器**：含 `yield` 的函数。调用它返回一个生成器对象（同时是迭代器），函数体
在每次 `next()` 时执行到下一个 `yield` 暂停。天然惰性——一次只保留一个值。

```python
def read_ints(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield int(line)
```

**生成器管道**：生成器可以串联，形成惰性数据流：

```python
nums = read_ints("data/numbers.txt")
evens = (n for n in nums if n % 2 == 0)
squared = (n * n for n in evens)   # 到这里都还没真正读文件
```

`yield from sub_iter` 把迭代委托给子迭代器，简化嵌套。

## 本模块练习（见 `exercises.py`）
1. `running_max`：产出到目前为止的运行最大值
2. `chunk`：把可迭代对象按固定大小切块
3. `revenue_by_region`：惰性解析 `data/sales.csv`，按地区汇总营收（units×price）

运行示例：`python lessons/01_iterators_generators/examples.py`
做完练习后：`pytest tests/test_01_iterators_generators.py`
