# Lesson 16 · 综合项目（Capstone，雏形）

把前面各课的机制组合成一个**可运行、可测试、可讲解**的小工具。三个选题任选其一；
本目录已内置 **选题 A 的可运行雏形**，B/C 给出设计说明供你实现。

## 选题 A：Course Resource Pack Checker（已内置雏形）
检查每个 lesson 是否包含标准资源文件（`metadata.yml`、`README.md`、`examples.py`、
`exercises.py`、`solutions.py`），汇总缺失项并生成报告。可直接作为课程质量检查工具。

**会用到**：pathlib、dataclass、iterator/generator、context manager、logging、pytest、CLI。

**运行**：
```bash
python -m lessons.16_capstone_project.solutions --root lessons --format markdown
```

`solutions.py` 提供了核心 API：`check_lesson()` / `check_course()` / `format_report()`，
`exercises.py` 是同名骨架，测试见 `tests/test_16_capstone_project.py`。

## 选题 B：Log Analyzer Toolkit（设计说明）
读取 `data/access.log`，按 IP / 路径 / 状态码 / 时间段统计，支持大文件流式处理，
输出 CSV/JSON 报告。会用到 generator pipeline、正则、logging、测试、CLI。

## 选题 C：Mini Async Book Enricher（设计说明）
读取 `data/books.json`，异步模拟请求图书详情，限制并发、处理 timeout，输出增强后的
JSON。会用到 dataclass、type hints、asyncio、异常处理、序列化、pytest。

## 交付要求（三选题通用）
- 一个可执行命令（`python -m ...` 或 console script）。
- 对应的 pytest 测试。
- 一段 README，说明如何运行与设计取舍。
