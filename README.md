# Python 高级程序设计

面向已掌握 Python 基础语法的学习者的进阶课程。聚焦语言的**高级特性**与
**工程实践**，每个模块都配有讲义、可运行示例、练习与参考解答，并使用 `data/`
下的真实小型数据集动手练习。

> 本仓库同时用作 Kabuqina 学习功能的课程资源样本：学习助手可读取代码、运行示例、
> 结合数据集辅导练习。

## 目录结构

```
python-advanced-course/
├── data/                     配套练习数据集（CSV / JSON / 日志 / 文本）
├── lessons/
│   ├── 01_iterators_generators/
│   ├── 02_decorators/
│   ├── 03_context_managers/
│   ├── 04_concurrency_asyncio/
│   ├── 05_metaprogramming/
│   ├── 06_dataclasses_typing/
│   ├── 07_functools_itertools/
│   └── 08_pattern_matching/
└── tests/                    校验各模块参考解答的 pytest
```

每个模块目录包含：

| 文件 | 作用 |
|------|------|
| `README.md` | 讲义：概念与要点 |
| `examples.py` | 可直接运行的演示（`python examples.py`） |
| `exercises.py` | 练习骨架（`raise NotImplementedError`，动手实现） |
| `solutions.py` | 参考解答（练习完再对照） |

## 模块

1. **迭代器与生成器** —— 迭代协议、惰性求值、`yield from`、流式处理大文件
2. **装饰器与闭包** —— 高阶函数、`functools.wraps`、带参装饰器、缓存与计时
3. **上下文管理器** —— `with`、`__enter__/__exit__`、`contextlib`、确定性资源释放
4. **并发与 asyncio** —— GIL、线程 vs 进程、事件循环、`async/await`、`gather`
5. **元编程** —— 描述符、`__set_name__`、`property`、元类与 `__init_subclass__`
6. **数据类与类型协议** —— `@dataclass`、`frozen/order`、`__post_init__` 校验、`typing.Protocol`
7. **functools 与 itertools** —— `lru_cache`、`reduce`、`singledispatch`、惰性迭代组合
8. **结构化模式匹配** —— `match/case`、映射/序列模式、捕获与守卫（Python 3.10+）

## 快速开始

```bash
python -m venv .venv
. .venv/Scripts/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 运行某个模块的演示
python lessons/01_iterators_generators/examples.py

# 做练习：编辑 exercises.py，然后跑测试
pytest
```

## 数据集

见 [`data/README.md`](data/README.md)。数据均为小型、真实结构的占位数据，供练习使用，
可随时替换为你自己的数据。

## 许可证

MIT，见 [LICENSE](LICENSE)。
