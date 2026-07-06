# Lesson 00 讲义 · 课程导入与仓库运行

## 1. 这门课学什么
你已经会写 Python 脚本。这门课要把你从“能写脚本”推进到“能写**可维护、可测试、
可解释**的工程代码”。主线不是“高级语法大全”，而是：

> 理解 Python 的运行机制，并用这些机制写出可维护、可测试、可扩展、可被学习助手解释的代码。

## 2. 环境准备
- **虚拟环境**（venv）：把项目依赖与系统 Python 隔离，避免版本互相污染。
  ```bash
  python -m venv .venv
  . .venv/Scripts/activate          # PowerShell: .venv\Scripts\Activate.ps1
  ```
- **依赖安装**：`pip install -r requirements.txt`（本课程只依赖 `pytest`）。
- **`python -m`**：以模块方式运行，能正确设置导入路径，例如 `python -m pytest`。

## 3. 仓库结构
```text
lessons/   每课一个资源包（讲义 / 示例 / 练习 / 解答 / 卡片 / 思维导图）
data/      小型真实结构数据（CSV / JSON / 日志 / 文本）
tests/     校验各课参考解答的 pytest；course_loader.py 负责按目录加载
```
测试通过 `tests/course_loader.py` 的 `load("<lesson_dir>")` 按**文件路径**加载
每课的 `solutions.py`，因此不同课可以有同名文件而不冲突。

## 4. 学习循环
1. 读 `README.md` / `lecture.md` 建立概念。
2. `python lessons/<课>/examples.py` 观察可运行示例。
3. 在 `exercises.py` 里实现函数（骨架用 `raise NotImplementedError`）。
4. `pytest tests/test_<课>.py` 验证；红→绿。
5. 对照 `solutions.py` 复盘。

## 5. 常见错误
- 忘记激活虚拟环境，导致 `pip install` 装到全局或找不到 `pytest`。
- 在错误的工作目录运行，导致相对路径（如 `data/…`）找不到文件——示例里统一用
  `Path(__file__).resolve().parents[...]` 定位，避免依赖当前目录。
- 以为“测试通过=万事大吉”：测试只覆盖它检查的场景，边界仍需自己思考。
