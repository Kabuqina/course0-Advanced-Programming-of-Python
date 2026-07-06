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
│   └── 05_metaprogramming/
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

## 课程结构升级（Phase 1）

仓库正按 [`course_structure.md`](course_structure.md) 的 17 课蓝图逐步升级。**第一阶段**
已落地 6 个核心课 + 1 个综合项目雏形，每课都是标准资源包
（`metadata.yml` / `README.md` / `lecture.md` / `examples.py` / `exercises.py` /
`solutions.py` / `kabuqina_cards.md` / `mindmap.mmd` + `tests/`）：

| 新课 | 目录 | 说明 |
|------|------|------|
| 00 | `00_orientation` | 课程导入与仓库运行 |
| 01 | `01_objects_names_mutability` | 对象、名字与可变性 |
| 03 | `03_iterators_generators` | 迭代器与生成器（迁移自旧 `01_`） |
| 05 | `05_decorators` | 装饰器与闭包（迁移自旧 `02_`） |
| 06 | `06_context_managers` | 上下文管理器（迁移自旧 `03_`） |
| 11 | `11_testing_pytest` | 测试与 pytest |
| 16 | `16_capstone_project` | 综合项目雏形（资源包检查器） |

> 迁移期间旧目录（`01_iterators_generators`、`02_decorators`、`03_context_managers`、
> `04_concurrency_asyncio`、`05_metaprogramming`）暂**保留并存**，待新结构稳定后再合并。

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
