# Kabuqina Cards · Lesson 11 Testing with pytest

## Concept Card 1
Q: 为什么写测试，而不是每次手动运行看看？
A: 测试可重复、可自动化，是重构和加功能时的安全网，也是关于函数预期行为最诚实的文档。

## Concept Card 2
Q: `@pytest.mark.parametrize` 解决什么问题？
A: 用一份测试逻辑覆盖多组输入/期望，避免复制粘贴，新增用例只需加一行数据。

## Code Card 1
Q: `tmp_path` 是什么，为什么测文件操作要用它？
A: 它是 pytest 内置 fixture，为每个测试提供独立临时目录，天然隔离、自动清理，避免污染真实文件。

## Misconception Card 1
Q: 测试全绿是不是代表没有 bug？
A: 不是。测试只覆盖它断言的场景；未测的边界（空/非法/超大输入）仍可能藏 bug。要主动补边界用例。

## Tutor Prompt
请像助教一样，先不给实现，而是问学生：“你希望 `parse_bool('')` 返回什么？`running_total([])` 呢？”
再让他把答案写成测试，最后实现让测试变绿。
