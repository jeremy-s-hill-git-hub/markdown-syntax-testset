# GFM 扩展

本文件测试 GFM 相对 CommonMark 新增的扩展。
GFM 是 CommonMark 的严格超集，扩展共 5 个：表格、任务列表、删除线、自动链接、禁用原始 HTML。
CommonMark 已有的语法不在此重复测试，见 `00-commonmark/`。

示例文字一律用英文，说明文字用中文。

## 表格

T:基本表格 | 源 GFM 0.29-gfm §4.10  
预期 渲染为两列两行表格，首行为表头 | 流行度 A

| Column one | Column two |
| --- | --- |
| Alpha | Beta |

T:对齐：左中右 | 源 GFM 0.29-gfm §4.10  
预期 三列分别左、中、右对齐 | 流行度 A

| Left | Center | Right |
| :--- | :---: | ---: |
| a | b | c |

T:首尾管道可省略 | 源 GFM 0.29-gfm §4.10  
预期 与带管道写法渲染一致 | 流行度 B

Column one | Column two
--- | ---
Alpha | Beta

T:单元格宽度无需对齐 | 源 GFM 0.29-gfm §4.10  
预期 短横线数量不影响渲染 | 流行度 B

| a | b |
| - | - |
| a longer cell | x |

T:管道可转义 | 源 GFM 0.29-gfm §4.10  
预期 单元格内显示竖线，不拆列 | 流行度 B

| With a pipe |
| --- |
| a \| b |

T:转义管道在代码跨度内 | 源 GFM 0.29-gfm §4.10  
预期 代码内显示竖线 | 流行度 C

| Pipe inside code |
| --- |
| `a \| b` |

T:表头与分隔行列数不一致则不成立 | 源 GFM 0.29-gfm §4.10  
预期 不渲染为表格，显示为原文 | 流行度 B

| a | b |
| --- |
| 1 | 2 |

T:数据行列数可多可少 | 源 GFM 0.29-gfm §4.10  
预期 少者补空单元格，多者忽略多余 | 流行度 B

| a | b |
| --- | --- |
| only one cell |
| one | two | three |

T:空行终止表格 | 源 GFM 0.29-gfm §4.10  
预期 表格在上，空行后文字成为独立段落 | 流行度 B

| a | b |
| --- | --- |
| 1 | 2 |

This text after the blank line is no longer part of the table.

T:表格内不可含块级元素 | 源 GFM 0.29-gfm §4.10  
预期 块级语法在单元格内按行内处理或原文显示 | 流行度 C

| Header |
| --- |
| # not a heading |

T:单元格内可行内语法 | 源 GFM 0.29-gfm §4.10  
预期 单元格内的粗体与代码生效 | 流行度 B

| Syntax | Example |
| --- | --- |
| Bold | **bold** |
| Code | `code` |

T:仅表头无数据行 | 源 GFM 0.29-gfm §4.10  
预期 只渲染表头，无数据行 | 流行度 C

| Header only |
| --- |
| |

## 任务列表

T:未勾选与已勾选 | 源 GFM 0.29-gfm §5.3  
预期 出现两个复选框，前者未选后者已选 | 流行度 A

- [ ] An open task
- [x] A completed task

T:大写 X 同样有效 | 源 GFM 0.29-gfm §5.3  
预期 复选框被勾选 | 流行度 B

- [X] Uppercase X is completed too

T:方括号内为空格的必须是空白 | 源 GFM 0.29-gfm §5.3  
预期 未勾选 | 流行度 B

- [ ] A space means unchecked

T:非空格非 x 不构成任务项 | 源 GFM 0.29-gfm §5.3  
预期 不渲染复选框，方括号按原文显示 | 流行度 B

- [y] Not a valid task marker

T:有序列表任务项 | 源 GFM 0.29-gfm §5.3  
预期 带编号并列复选框 | 流行度 B

1. [ ] First step
2. [x] Second step

T:任务列表嵌套 | 源 GFM 0.29-gfm §5.3  
预期 两层复选框，各自状态独立 | 流行度 B

- [x] Parent task
  - [ ] First child task
  - [x] Second child task

T:标记后必须有空白 | 源 GFM 0.29-gfm §5.3  
预期 无空白则不构成任务项，方括号按原文显示 | 流行度 C

- [x]marker touching the text

## 删除线

T:双波浪线删除线 | 源 GFM 0.29-gfm §6.5  
预期 文字带删除线 | 流行度 A

~~struck through text~~

T:单波浪线同样有效 | 源 GFM 0.29-gfm §6.5  
预期 文字带删除线 | 流行度 B

~single tilde strikethrough~

T:三个及以上波浪线不构成 | 源 GFM 0.29-gfm §6.5  
预期 波浪线按原文显示 | 流行度 B

These three tildes ~~~do not strike~~~ should stay literal.

T:删除线不能跨段落 | 源 GFM 0.29-gfm §6.5  
预期 两个段落各显示波浪线原文 | 流行度 C

This paragraph has ~~an unclosed strikethrough

A new paragraph~~here the tildes are literal

T:删除线内可含其他行内语法 | 源 GFM 0.29-gfm §6.5  
预期 删除线内出现粗体 | 流行度 B

~~struck through with **bold** inside~~

T:删除线与强调可嵌套 | 源 GFM 0.29-gfm §6.5  
预期 同时呈现斜体与删除线 | 流行度 C

*italic with ~~strikethrough~~ inside*

## 自动链接（扩展）

T:www 自动链接 | 源 GFM 0.29-gfm §6.9  
预期 自动成为链接，补全 http:// | 流行度 A

www.commonmark.org

T:带路径的 www 自动链接 | 源 GFM 0.29-gfm §6.9  
预期 路径一并成为链接的一部分 | 流行度 B

Visit www.commonmark.org/help for details

T:协议开头的裸链接 | 源 GFM 0.29-gfm §6.9  
预期 整段成为可点击链接 | 流行度 A

https://example.com/path?q=1

T:行尾标点不纳入链接 | 源 GFM 0.29-gfm §6.9  
预期 末尾句号留在链接之外 | 流行度 B

Visit www.commonmark.org.

T:邮箱自动链接 | 源 GFM 0.29-gfm §6.9  
预期 成为 mailto 链接 | 流行度 A

foo@bar.baz

T:加号可在 @ 前不可在 @ 后 | 源 GFM 0.29-gfm §6.9  
预期 前者成链接，后者不成 | 流行度 C

hello+xyz@mail.example and hello@mail+xyz.example

T:行首非空白处不自动链接 | 源 GFM 0.29-gfm §6.9  
预期 紧贴前文时不成链接 | 流行度 C

textwww.commonmark.org

T:括号配对影响链接边界 | 源 GFM 0.29-gfm §6.9  
预期 多余的右括号留在链接外 | 流行度 D

(www.example.com/search?q=test))

## 禁用原始 HTML

T:危险标签被替换 | 源 GFM 0.29-gfm §6.11  
预期 script 标签的尖括号被转义为文本，不执行 | 流行度 A

<script>tag content</script>

T:普通标签不受影响 | 源 GFM 0.29-gfm §6.11  
预期 strong 与 em 正常生效 | 流行度 A

<strong>bold</strong> and <em>italic</em>

T:iframe 被过滤 | 源 GFM 0.29-gfm §6.11  
预期 显示为转义文本，不加载 | 流行度 B

<iframe src="https://example.com"></iframe>

T:style 标签被过滤 | 源 GFM 0.29-gfm §6.11  
预期 显示为转义文本，不生效 | 流行度 B

<style>body { color: red; }</style>

T:大小写不影响过滤 | 源 GFM 0.29-gfm §6.11  
预期 大写标签同样被转义 | 流行度 C

<SCRIPT>uppercase tag</SCRIPT>

T:未闭合波浪线按原文 | 源 GFM 0.29-gfm §6.5  
预期 波浪线原样显示，不吞掉后续 | 流行度 C

Here is an ~~unclosed strikethrough and the text after it should still be visible.
