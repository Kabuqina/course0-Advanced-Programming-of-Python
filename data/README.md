# 数据集

配套练习使用的小型数据文件，结构真实、体积小，便于动手与测试。

下表 **used_by** 采用升级后的新课编号（见 [`../course_structure.md`](../course_structure.md)）；
迁移期间的旧模块编号一并列出，便于对照。

| 文件 | 格式 | 用于（新课） | 旧模块 | 说明 |
|------|------|------|------|------|
| `numbers.txt` | 每行一个整数 | Lesson 03（迭代器）、06（上下文管理器示例） | 模块 1、3 | 流式读取、生成器聚合 |
| `sales.csv` | CSV（含表头） | Lesson 03（迭代器）、04（管道，规划中） | 模块 1 | 惰性解析、分组求和 |
| `access.log` | 类 Apache 访问日志 | Lesson 05（装饰器）、16 选题 B | 模块 2 | 逐行解析、按状态码统计 |
| `books.json` | JSON 数组 | Lesson 16 选题 C（异步增强）、09/15（规划中） | 模块 4、5 | 异步抓取模拟、字段校验（描述符） |
| `employees.csv` | CSV（含表头） | Lesson 09（数据类，规划中） | 模块 6 | 解析为数据类、按部门分组 |
| `events.json` | JSON 数组 | 结构化模式匹配（规划中） | 模块 8 | `match/case` 事件分类统计 |

字段说明：

- **sales.csv**：`date, region, product, units, price`
- **access.log**：`IP - - [time] "METHOD path HTTP/1.1" status bytes`
- **books.json**：每项 `{ "title", "author", "year", "price", "tags" }`
- **employees.csv**：`id, name, department, salary, hired`
- **events.json**：每项 `{ "type", ... }`，type 决定其余字段（click/key/scroll/resize）

这些是占位数据，可替换为你自己的真实数据集而无需改动练习代码。
