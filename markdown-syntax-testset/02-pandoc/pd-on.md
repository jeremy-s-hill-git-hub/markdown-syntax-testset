---
title: Markdown Syntax Testset - Pandoc Default Extensions
author: Example Author
date: 2026-11-01
---

# Pandoc 默认开启的扩展

本文件测试 Pandoc 的 `markdown` 格式**默认即生效**的扩展。
未特别说明的语法，在 Pandoc 中直接可用；在普通编辑器里通常退化为纯文本。

示例文字一律用英文，说明文字用中文。
本文件开头的元数据块就是一个用例，见 T:YAML 元数据块。

## 定义列表

T:定义列表基本形态 | 源 PM §definition_lists  
预期 出现术语与释义的对照结构 | 流行度 A

Term one

:   The definition of term one.

Term two

:   The definition of term two.

定义列表是 Pandoc 的标志性扩展之一。
CommonMark 与 GFM 都没有这个语法，标记是冒号加缩进。

## 行内上下标

T:上标 | 源 PM §superscript-subscript  
预期 文字升高显示 | 流行度 A

The chemical formula of water is H~2~O and the energy formula is E = mc^2^.

T:下标与上标可在同一段混用 | 源 PM §superscript-subscript  
预期 两者各自按位置显示 | 流行度 B

x~1~ and x^2^ are at different positions in the same paragraph.

这两个扩展在程序输出里是分开的两条：`superscript` 与 `subscript`。
手册则合并写作一条 `superscript-subscript`。

## 删除线

T:双波浪线删除 | 源 PM §strikeout  
预期 文字带删除线 | 流行度 A

~~struck through text~~

T:单波浪线在 Pandoc 中同样有效 | 源 PM §strikeout  
预期 文字带删除线 | 流行度 B

~a single tilde strikes this out~

注意：GFM 与 Pandoc 都支持单双波浪线，但两者对三波浪线的处理不同。
行首的三波浪线在两者中都会被当作围栏，因此不要在行首写。

## 数学公式

T:行内公式 | 源 PM §tex_math_dollars  
预期 公式被渲染为数学排版，或原样显示 | 流行度 A

The mass-energy relation is $E = mc^2$ written inline.

T:行间公式 | 源 PM §tex_math_dollars  
预期 公式独占一行并居中排版 | 流行度 A

The display formula follows:

$$\int_0^1 x^2 \, dx = \frac{1}{3}$$

若编辑器不支持数学，上面两段会显示为带美元符号的原文。
这本身就是一个可判读的降级结果。

## 表格的四种形态

T:管道表格 | 源 PM §pipe_tables  
预期 渲染为表格 | 流行度 A

| Left column | Right column |
|:------------|-------------:|
| Alpha       | Beta         |

T:简单表格 | 源 PM §simple_tables  
预期 渲染为表格 | 流行度 B

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123

T:多行表格 | 源 PM §multiline_tables  
预期 单元格内容可跨行 | 流行度 C

-------------------------------------------------------------
 Centered   Default           Right Left
  Header    Aligned         Aligned Aligned
----------- ------- --------------- -------------------------
   First    row                12.0 Example of a row that
                                    spans multiple lines.

  Second    row                 5.0 Here is another one. Note
                                    the blank line between
                                    rows.
-------------------------------------------------------------

T:网格表格 | 源 PM §grid_tables  
预期 渲染为带边框的表格 | 流行度 C

+---------------+---------------+
| Fruit         | Price         |
+===============+===============+
| Bananas       | $1.34         |
+---------------+---------------+

T:表格标题 | 源 PM §table_captions  
预期 表格下方出现题注 | 流行度 B

| Variety | Price |
|---------|------:|
| Apple   |  3.00 |

: Fruit price table

四种表格语法并存是 Pandoc 的特点。
管道表格与 GFM 兼容，其余三种是 Pandoc 独有。

## 元数据与标题块

T:YAML 元数据块 | 源 PM §yaml_metadata_block  
预期 元数据被解析，不显示为正文 | 流行度 A

本文件最开头的那段 `---` 包围的内容就是元数据块。
它必须位于文档的最开头才生效，放在中间无效。

若支持，这三行不会出现在正文里；若不支持，降级结果不止一种：
开头那行 `---` 可能被当作分隔线，中间几行变成段落，
而结尾那行 `---` 紧跟文字，可能把这几行变成二级标题。测量时应留意这几种形态。

T:传统标题块 | 源 PM §pandoc_title_block  
预期 标题信息被单独提取 | 流行度 C

% Document title
% Author one; Author two
% 2026-11-01

这是 Pandoc 较早的标题写法，用百分号起头。
它同样必须位于文档开头才生效，因此本处的写法只是演示，不会被解析。

## 标题属性

T:标题后接标识符 | 源 PM §header_attributes  
预期 标题带自定义锚点 | 流行度 A

### A heading with an identifier {#custom-anchor}

上面的花括号部分应被解析为属性而不显示。

T:标题后接类名 | 源 PM §header_attributes  
预期 标题附带类名 | 流行度 B

### A heading with class names {.special .highlighted}

## 围栏代码块与属性

T:围栏加属性 | 源 PM §fenced_code_attributes  
预期 代码块附带标识与类名 | 流行度 B

```{#mycode .python .numberLines}
def example():
    return 42
```

T:行内代码加属性 | 源 PM §inline_code_attributes  
预期 行内代码附带类名 | 流行度 C

This is inline code `x = 1`{.python} with an attribute.

## 围栏 div 与方括号 span

T:围栏 div | 源 PM §fenced_divs  
预期 内容被包裹为块级容器，可能带边框或样式 | 流行度 B

::: warning
This paragraph is wrapped by three colons and forms a block level container.
:::

T:方括号 span | 源 PM §bracketed_spans  
预期 文字被包裹为行内容器 | 流行度 C

This paragraph has [wrapped text]{.highlight} as an inline marker.

这两种写法在 Pandoc 之外通常显示为原文。
它们与 CommonMark 的冒号无冲突，因为 CommonMark 不赋予其含义。

## 脚注

T:引用式脚注 | 源 PM §footnotes  
预期 正文出现脚注编号，文末出现脚注内容 | 流行度 A

Here is a footnote reference[^note-a] pointing to the definition below.

[^note-a]: This is the footnote content, usually shown at the bottom of the page.

T:行内脚注 | 源 PM §inline_notes  
预期 脚注内容直接写在引用处 | 流行度 B

This is an inline footnote^[The content is embedded directly at the reference position.] form.

## 引用与文献

T:文献引用 | 源 PM §citations  
预期 显示为作者年份或编号 | 流行度 C

This sentence cites a reference [@doe2020].

文末通常需要参考文献定义，此处不展开。

## 行块

T:行块保留换行 | 源 PM §line_blocks  
预期 每行原样保留，不合并为段落 | 流行度 C

| The first line is preserved as is
| The second line is preserved as is
| The third line is preserved as is

竖线起头的每一行都是一个独立的行块。

## 其他默认开启项

T:强调词内的下划线 | 源 PM §intraword_underscores  
预期 下划线不被当作强调 | 流行度 B

The underscore in snake_case_name should not trigger italics.

T:智能标点 | 源 PM §smart  
预期 直引号变为弯引号，短横变为破折号 | 流行度 B

"Straight quotes" and 'single quotes', as well as -- and ---.

T:任意符号可转义 | 源 PM §all_symbols_escapable  
预期 反斜杠使符号失去语法含义 | 流行度 C

\A and \1 can also be escaped in Pandoc, whereas CommonMark only escapes punctuation.

T:隐式标题引用 | 源 PM §implicit_header_references  
预期 方括号文字自动链接到同名标题 | 流行度 C

See the section [定义列表](#定义列表) for details.

## 小结

以上语法在 Pandoc 的 markdown 格式下默认生效。
用 markdown_strict 格式则大部分失效，这正是与原版 Markdown 的差别所在。
默认关闭的扩展见 `pd-off.md`。
