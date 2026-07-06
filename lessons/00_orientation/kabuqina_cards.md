# Kabuqina Cards · Lesson 00 Orientation

## Concept Card 1
Q: 为什么要用虚拟环境（venv）？
A: 把本项目的依赖与系统/其他项目隔离，避免版本冲突，保证“在我机器上能跑”可复现。

## Concept Card 2
Q: `python script.py` 和 `python -m module` 有什么区别？
A: `-m` 以模块方式运行并把当前目录纳入导入路径，常用于 `python -m pytest`、`python -m venv`。

## Code Card 1
Q: 示例为什么用 `Path(__file__).resolve().parents[2]` 而不是相对路径？
A: 这样定位仓库根目录不依赖“当前工作目录”，无论从哪运行都能找到 data/ 与 lessons/。

## Misconception Card 1
Q: 测试全绿是不是就说明代码完全正确？
A: 不是。测试只覆盖它断言的场景，未覆盖的边界（空输入、异常、超大数据）仍需自己考虑。

## Tutor Prompt
请像助教一样，先让学生运行 `python lessons/00_orientation/examples.py`，
再问：“输出里的解释器路径是否指向你的 .venv？如果不是，说明什么？”
