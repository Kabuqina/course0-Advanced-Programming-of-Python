# 数据集

配套练习使用的小型数据文件，结构真实、体积小，便于动手与测试。

| 文件 | 格式 | 用于 | 说明 |
|------|------|------|------|
| `numbers.txt` | 每行一个整数 | 模块 1 | 流式读取、生成器聚合 |
| `sales.csv` | CSV（含表头） | 模块 1 | 惰性解析、分组求和 |
| `access.log` | 类 Apache 访问日志 | 模块 2 | 逐行解析、按状态码统计 |
| `books.json` | JSON 数组 | 模块 4、5 | 异步抓取模拟、字段校验（描述符） |

字段说明：

- **sales.csv**：`date, region, product, units, price`
- **access.log**：`IP - - [time] "METHOD path HTTP/1.1" status bytes`
- **books.json**：每项 `{ "title", "author", "year", "price", "tags" }`

这些是占位数据，可替换为你自己的真实数据集而无需改动练习代码。
