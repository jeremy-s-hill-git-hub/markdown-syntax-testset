Title: Other Dialects
Author: Example Author
Date: 2026-11-01

# 其他方言独有语法

本文件测试 MultiMarkdown、Markdown Extra、Kramdown 三种方言中尚未被 CommonMark、GitHub、Pandoc 覆盖的独有语法。
脚注、定义列表、数学、引用、缩写、属性等已归 GitHub 或 Pandoc 维度，此处不重测。
MDX 与 R Markdown 需 JS 编译或 knitr 执行环境，不在裸渲染测试范围。
示例文字一律用英文，说明文字用中文。

## MultiMarkdown

MultiMarkdown 支持文档开头的元数据头（`key: value`），它以空行结束、只在文档最前方生效；正文中可用 `[%key]` 引用元数据值。本文件最开头三行即这种元数据头。

T:元数据头 | 源 MMD v5 Metadata  
预期 元数据被解析，不显示为正文 | 流行度 B

T:元数据变量引用 | 源 MMD v5 Metadata  
预期 方括号变量被替换为对应元数据值 | 流行度 C

This document is written by [%author] on [%date].

## Markdown Extra

Markdown Extra 允许在 HTML 块上写 `markdown="1"`，使块内文字按 Markdown 解析；围栏代码块可在语言标记位置直接写类名（无花括号）。

T:HTML 块内 Markdown | 源 Extra Markdown Inside HTML Blocks  
预期 属性被剥离，div 内文字按 Markdown 渲染 | 流行度 B

<div markdown="1">
This is *true* markdown text.
</div>

T:围栏类名（无花括号） | 源 Extra Fenced Code Blocks  
预期 代码块获得 html 类名；与 Pandoc 的花括号形式不同 | 流行度 C

~~~~ .html
<p>a paragraph with emphasis</p>
~~~~

## Kramdown

Kramdown 用属性列表（IAL）为块级或行内元素附加 id 与类名，属性行本身不显示。

T:块级属性列表 | 源 Kramdown Block IAL  
预期 前一段落获得 id，属性行本身不显示 | 流行度 B

A paragraph that receives an id attribute.
{: #para-one}

T:行内属性列表 | 源 Kramdown Span IAL  
预期 强调部分附加类名，属性不显示 | 流行度 B

This *is*{:.underline} an inline attribute example.
