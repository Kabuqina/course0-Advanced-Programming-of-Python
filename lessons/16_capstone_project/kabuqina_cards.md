# Kabuqina Cards · Lesson 16 Capstone

## Concept Card 1
Q: 综合项目的重点是什么？
A: 不是学新语法，而是把已学机制（pathlib、dataclass、生成器、上下文管理器、logging、测试、CLI）组织成一个可运行、可测试、可讲解的小工具。

## Concept Card 2
Q: 为什么要把 `check_course`（逻辑）和 `format_report`（呈现）分开？
A: 逻辑纯、无副作用，便于单测；呈现层可自由换 markdown/JSON 而不动逻辑。关注点分离让代码更易维护。

## Code Card 1
Q: 检查器为什么用生成器 `iter_lesson_dirs` 遍历目录？
A: 惰性遍历，不必一次性构造整份列表；数据量大时更省内存，也更符合课程强调的“流式思维”。

## Tutor Prompt
请像项目导师一样，先让学生说清工具“做什么/输入什么/输出什么”，
再引导他按“数据模型 → 纯逻辑 → 遍历 → 输出 → CLI → 测试”逐层实现，每层配一个测试。
