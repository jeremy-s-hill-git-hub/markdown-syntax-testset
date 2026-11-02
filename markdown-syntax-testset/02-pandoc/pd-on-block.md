---
title: Markdown Syntax Testset - Pandoc Default Extensions
author: Example Author
date: 2026-11-01
---

# Pandoc 默认开启的扩展·块级

本文件测试 Pandoc 的 `markdown` 格式默认即生效、且属于块级的扩展。
未特别说明的语法在 Pandoc 中直接可用，在普通编辑器里通常退化为纯文本。
行内扩展见 `pd-on-inline.md`，表格见 `pd-on-table.md`，默认关闭项见 `pd-off-block.md`。
数学与脚注已归 GitHub 维度，见 `01-github/gh-ext.md`。
示例文字一律用英文，说明文字用中文。

## 元数据与标题块

YAML 元数据块用 `---` 包围，必须位于文档最开头才生效；传统标题块用百分号起头，同样只在开头生效。二者被解析后不作为正文显示。

T:YAML 元数据块 | 源 PM yaml_metadata_block  
预期 元数据被解析，不显示为正文 | 流行度 A

本文件最开头的那段 `---` 包围的内容就是元数据块，它必须位于文档最开头才生效，放在中间无效。

T:传统标题块 | 源 PM pandoc_title_block  
预期 标题信息被单独提取 | 流行度 C

% Document title
% Author one; Author two
% 2026-11-01

这是 Pandoc 较早的标题写法，用百分号起头；同样必须位于文档开头才生效，因此本处只是演示，不会被解析。

## 标题属性

标题属性写在标题行末尾的花括号里，可指定标识符、类名与键值对；它们被解析为属性而不显示。

T:标题后接标识符 | 源 PM header_attributes  
预期 标题带自定义锚点 | 流行度 A

### A heading with an identifier {#custom-anchor}

T:标题后接类名 | 源 PM header_attributes  
预期 标题附带类名 | 流行度 B

### A heading with class names {.special .highlighted}

## 围栏代码属性

围栏代码块可在起始围栏后写属性，指定标识符、类名与选项；行内代码属性见行内文件。

T:围栏加属性 | 源 PM fenced_code_attributes  
预期 代码块附带标识与类名 | 流行度 B

```{#mycode .python .numberLines}
def example():
    return 42
```

## 围栏 div

三个及以上冒号包裹一块内容，形成块级容器，可带类名或标识符；在 Pandoc 之外通常显示为原文。

T:围栏 div | 源 PM fenced_divs  
预期 内容被包裹为块级容器，可能带边框或样式 | 流行度 B

::: warning
This paragraph is wrapped by three colons and forms a block level container.
:::

## 原生 div

不带属性的冒号围栏形成原生 div 容器，语义与围栏 div 相同，但不附加类名。

T:原生 div | 源 PM native_divs  
预期 内容被包裹为块级容器 | 流行度 C

::::
A native div without attributes, delimited by four colons.
::::

## 行块

行块用竖线起头，每一行原样保留，不合并为段落。

T:行块保留换行 | 源 PM line_blocks  
预期 每行原样保留，不合并为段落 | 流行度 C

| The first line is preserved as is
| The second line is preserved as is
| The third line is preserved as is

## 定义列表

定义列表用术语行加冒号缩进的释义构成，是 Pandoc 的标志性扩展；CommonMark 与 GFM 都没有这个语法。

T:定义列表基本形态 | 源 PM definition_lists  
预期 出现术语与释义的对照结构 | 流行度 A

Term one

:   The definition of term one.

Term two

:   The definition of term two.

## 花式列表

开启 fancy_lists 后，有序列表除数字外还支持字母与罗马数字标记，无序列表支持更多符号。

T:字母与罗马数字标记 | 源 PM fancy_lists  
预期 按字母或罗马数字编号 | 流行度 C

(a) Alpha item
(b) Beta item

i. Roman one
ii. Roman two

## 示例列表

示例列表用 `(@标签)` 形式命名每一项，供正文引用；未命名的项按连续示例编号。

T:示例列表 | 源 PM example_lists  
预期 渲染为带编号的示例列表 | 流行度 D

(@) First example
(@) Second example

## 标题前需空行

Pandoc 要求标题前有空行，否则井号开头的行可能被当作上一段的续行；这是为了避免误把行首井号识别为标题。

T:无空行时井号不构成标题 | 源 PM blank_before_header  
预期 显示为段落续行，不是标题 | 流行度 B

I like several of their flavors of ice cream:
#22, for example, and #5.

T:有空行时构成标题 | 源 PM blank_before_header  
预期 渲染为标题 | 流行度 B

A sentence before the heading.

## A heading after a blank line

## 引用前需空行

Pandoc 同样要求引用块前有空行，否则大于号行可能被并入上一段。

T:无空行时大于号不构成引用 | 源 PM blank_before_blockquote  
预期 显示为段落续行 | 流行度 C

A sentence that ends here.
> This greater-than line follows without a blank line.

## HTML 块内 Markdown

Pandoc 默认在 HTML 块内解析 Markdown（CommonMark 不解析），因此块内的强调等语法会生效。

T:HTML 块内解析 Markdown | 源 PM markdown_in_html_blocks  
预期 块内强调生效 | 流行度 B

<div>
*This text is emphasized inside the div.*
</div>

## 原始 LaTeX

Pandoc 允许直接嵌入原始 LaTeX 命令；不渲染 LaTeX 的编辑器会原样显示。

T:块级原始 LaTeX | 源 PM raw_tex  
预期 按 LaTeX 处理，或原样显示 | 流行度 C

\begin{equation}
a^2 + b^2 = c^2
\end{equation}

T:围栏原始属性 | 源 PM raw_attribute  
预期 内容按指定格式输出，或原样显示 | 流行度 C

```{=latex}
\textbf{raw latex content}
```

T:LaTeX 宏定义 | 源 PM latex_macros  
预期 宏被记录并可用于后续公式，或原样显示 | 流行度 D

\newcommand{\R}{\mathbb{R}}

## 自动标识符

Pandoc 为每个标题自动生成标识符，供内部链接与锚点使用；默认算法与 GFM 不同，见 `pd-off-inline.md` 的 gfm_auto_identifiers。

T:标题自动生成标识符 | 源 PM auto_identifiers  
预期 标题获得可用于跳转的标识符 | 流行度 B

### A heading with Chinese 中文 and English
