# Markdown 语法测试集

本目录是 Markdown 语法测试集，本文件是其中的索引。
全文只用最基础的语法，因此它本身也是一个基础测试用例。

## 导航

- [块级结构](00-commonmark/cm-block.md)
- [行内结构](00-commonmark/cm-inline.md)
- [边界与异常](00-commonmark/cm-edge.md)
- [吞噬型未闭合](00-commonmark/cm-eof.md)
- [GFM 扩展](01-gfm/gfm-ext.md)
- [GFM 与 CommonMark 的差异](01-gfm/gfm-edge.md)
- [Pandoc 默认开启的扩展](02-pandoc/pd-on.md)
- [Pandoc 默认关闭的扩展](02-pandoc/pd-off.md)
- [Mermaid 图表](03-editor-features/ef-mermaid.md)
- [GitHub Alerts](03-editor-features/ef-alerts.md)
- [CriticMarkup 修订标记](03-editor-features/ef-critic.md)
- [自动目录与 WikiLinks](03-editor-features/ef-toc-wikilinks.md)
- [其他方言独有语法](04-other-dialects/od-other.md)

以上都是子文件链接。下面这一条指向本文件内部，用作对照：

- [跳到基础语法](#基础语法)

对照的用法：若对照链接可点击而子文件链接不可点击，说明链接语法生效、问题出在路径；若两者都不可点击，说明链接语法本身不被支持。

## 基础语法

以下逐项演示本页用到的语法。
示例文字一律用英文，说明文字用中文，以便区分。

### 标题

本页用到一级到四级标题。以下是一个四级标题：

#### Sample heading level four

### 段落

First paragraph.

Second paragraph, separated from the previous one by a blank line.

### 无序列表

- First item
- Second item

### 链接

[Jump to basic syntax](#基础语法)

### 行内代码

`inline code`

### 强调

*italic* and **bold**

### 引用

> A single paragraph inside a block quote.

### 分隔线

---

以上为本页使用的全部语法。
