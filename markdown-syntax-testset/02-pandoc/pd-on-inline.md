# Pandoc 默认开启的扩展·行内

本文件测试 Pandoc 的 `markdown` 格式默认即生效、且属于行内的扩展。
数学与脚注已归 GitHub 维度，见 `01-github/gh-ext.md`；块级扩展见 `pd-on-block.md`，默认关闭项见 `pd-off-inline.md`。
示例文字一律用英文，说明文字用中文。

## 上下标

上标用插入符包裹、下标用波浪线包裹，二者可混用。Pandoc 把 superscript 与 subscript 列为两条扩展，手册合并写作一条。

T:上标 | 源 PM superscript  
预期 文字升高显示 | 流行度 A

The chemical formula of water is H~2~O and the energy formula is E = mc^2^.

T:下标与上标可在同一段混用 | 源 PM subscript  
预期 两者各自按位置显示 | 流行度 B

x~1~ and x^2^ are at different positions in the same paragraph.

## 行内代码属性

行内代码后可直接写属性，指定类名或标识符。

T:行内代码加属性 | 源 PM inline_code_attributes  
预期 行内代码附带类名 | 流行度 C

This is inline code `x = 1`{.python} with an attribute.

## 方括号 span

方括号 span 用方括号包裹文字并在其后写属性，形成行内容器；在 Pandoc 之外通常显示为原文。

T:方括号 span | 源 PM bracketed_spans  
预期 文字被包裹为行内容器 | 流行度 C

This paragraph has [wrapped text]{.highlight} as an inline marker.

## 原生 span

不带属性的方括号 span 形成原生行内容器，语义相同但不附加类名；视觉上可能无差异。

T:原生 span | 源 PM native_spans  
预期 文字被包裹为行内容器，视觉可能无差异 | 流行度 D

This paragraph has [plain wrapped text] as an inline native span.

## 行内脚注

行内脚注把脚注内容直接写在引用处，用插入符加方括号表示；它不同于 GitHub 的引用式脚注。

T:行内脚注 | 源 PM inline_notes  
预期 脚注内容直接写在引用处 | 流行度 B

This is an inline footnote^[The content is embedded directly at the reference position.] form.

## 文献引用

方括号内写 `@键` 表示文献引用，Pandoc 默认按作者年份或编号渲染。

T:文献引用 | 源 PM citations  
预期 显示为作者年份或编号 | 流行度 C

This sentence cites a reference [@doe2020].

## 强调词内的下划线

词内下划线不触发强调，以免与 snake_case 等标识符冲突。

T:强调词内的下划线 | 源 PM intraword_underscores  
预期 下划线不被当作强调 | 流行度 B

The underscore in snake_case_name should not trigger italics.

## 智能标点

智能标点把直引号替换为弯引号，把两个短横变为连接号、三个短横变为破折号。

T:智能标点 | 源 PM smart  
预期 直引号变为弯引号，短横变为破折号 | 流行度 B

"Straight quotes" and 'single quotes', as well as -- and ---.

## 任意符号可转义

Pandoc 允许用反斜杠转义任意符号，不只标点，使符号失去语法含义。

T:任意符号可转义 | 源 PM all_symbols_escapable  
预期 反斜杠使符号失去语法含义 | 流行度 C

\A and \1 can also be escaped in Pandoc, whereas CommonMark only escapes punctuation.

## 隐式标题引用

Pandoc 为每个标题自动建立引用，方括号内写标题文字即可链接过去。

T:隐式标题引用 | 源 PM implicit_header_references  
预期 方括号文字自动链接到同名标题 | 流行度 C

See the section [上下标] for details.

## 隐式图

段落中只含一张图片时，Pandoc 把它升级为带题注的图，题注取自替代文字。

T:隐式图 | 源 PM implicit_figures  
预期 图片带题注显示 | 流行度 C

![A caption that becomes the figure caption](../00-commonmark/media/placeholder.svg)

## 链接属性

链接后可直接写属性，为链接附加类名或标识符。

T:链接属性 | 源 PM link_attributes  
预期 链接附带类名 | 流行度 C

[an external link](https://example.com){.external}
