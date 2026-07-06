# Lesson 00 · 课程导入与仓库运行

## 目标
- 明确课程定位：**不是**重复基础语法，而是学习 Python 的“机制”和“工程化”。
- 跑通虚拟环境、依赖安装、示例运行、pytest。
- 理解仓库结构：`lessons/`、`data/`、`tests/`。

## 要点
- 每个 lesson 是一个**资源包**：讲义（README/lecture）、可运行示例（examples）、
  练习骨架（exercises）、参考解答（solutions）、测试（tests/）与小娜卡片（kabuqina_cards）。
- 学习循环：**读讲义 → 跑示例 → 做练习 → 跑测试 → 对照解答**。
- 测试校验的是 `solutions.py` 的参考实现；你在 `exercises.py` 里实现同名 API。

## 快速开始
```bash
python -m venv .venv
. .venv/Scripts/activate          # PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

python lessons/00_orientation/examples.py   # 环境自检
pytest tests/test_00_orientation.py          # 跑本课测试
```

## 本课练习（见 `exercises.py`）
1. `greet(name)`：修改一个简单函数让测试通过（体会“红→绿”）。
2. `python_at_least(major, minor)`：判断当前解释器版本是否达标。
3. 结合 `environment_report()` 给自己写一份 `environment_check.md`。

运行示例：`python lessons/00_orientation/examples.py`
做完练习后：`pytest tests/test_00_orientation.py`
