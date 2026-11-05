# Markdown 语法测试集

本目录是 Markdown 语法测试集，本文件既是总索引，也是基础语法的样例。
这一段本身是一个段落，用于验证段落渲染。

## 基础语法

### 段落

A paragraph is one or more lines of text
followed by a blank line.

### 标题

本文件以一级标题作标题，下面演示四级标题：

#### Sample heading level four

五级、六级标题同理，不单独占用层级。

### 无序列表

- First item
- Second item

### 有序列表

1. First step
2. Second step

### 引用

> A single paragraph inside a block quote.

### 分隔线

---

### 强调

*italic* and **bold**

### 行内代码

`inline code`

### 链接

[跳到基础语法](#基础语法)

## 子文件导航

测试集按平台与特性分目录，以下逐组列出各子文件的内容与位置。

1. CommonMark（核心语法）：规范主体（块级、行内）与边界异常（边界、吞噬型）；后者只收边界构造，不重复主体。
   - [块级结构](00-commonmark/cm-block.md) — 分隔线、标题、代码块、HTML 块、链接引用、段落、引用、列表
   - [行内结构](00-commonmark/cm-inline.md) — 转义、实体、代码跨度、强调、链接、图片、自动链接、原始 HTML、换行
   - [边界与异常](00-commonmark/cm-edge.md) — CommonMark 自身的边界与异常用例
   - [吞噬型未闭合](00-commonmark/cm-eof.md) — 文件末尾会吞掉后续内容的未闭合构造

2. GitHub（GFM 规范与 GitHub 扩展）：gfm-* 收规范内扩展，gfm-edge 只做与 CommonMark 的差异对比，gh-ext 收规范外特性；三者互不重复。
   - [GFM 扩展](01-github/gfm-ext.md) — 表格、任务列表、删除线、自动链接、危险标签
   - [GFM 与 CommonMark 差异](01-github/gfm-edge.md) — 两个规范的判定差异
   - [GitHub 非 GFM 扩展](01-github/gh-ext.md) — 数学公式、脚注、Emoji、Alerts、Mermaid 图表、折叠区块、HTML 上下标与下划线、相对链接、颜色模型

3. Pandoc：默认开启分块级、行内、表格，默认关闭分块级、行内；只收 Pandoc 独有扩展。
   - [默认开启的扩展·块级](02-pandoc/pd-on-block.md) — 元数据块、标题属性、围栏属性、div 与 span、行块
   - [默认开启的扩展·行内](02-pandoc/pd-on-inline.md) — 上下标、删除线、数学、脚注、引用、转义
   - [默认开启的扩展·表格](02-pandoc/pd-on-table.md) — 四种表格与题注
   - [默认关闭的扩展·块级](02-pandoc/pd-off-block.md) — 块级类关闭项
   - [默认关闭的扩展·行内](02-pandoc/pd-off-inline.md) — 行内类关闭项

4. 编辑器特性：与 GitHub 维度互补，只收非 GitHub 的通用编辑器约定。
   - [CriticMarkup 修订标记](03-editor-features/ef-critic.md)
   - [自动目录与 WikiLinks](03-editor-features/ef-toc-wikilinks.md)

5. 其他方言：只收 MMD、Extra、Kramdown 独有语法。
   - [其他方言独有语法](04-other-dialects/od-other.md) — MultiMarkdown、Markdown Extra、Kramdown

[跳到基础语法](#基础语法) — 自锚点对照：若此链接可点而上方子文件链接不可点，说明链接语法生效、问题在路径；若都不可点，说明链接语法不被支持。
