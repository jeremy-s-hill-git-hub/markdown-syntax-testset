# Pandoc 默认关闭的扩展·行内

本文件测试 Pandoc 的 `markdown` 格式下默认不生效、且属于行内的扩展。
这些语法在默认状态下按纯文本处理；在格式名后追加 `+扩展名` 后才生效。
块级关闭项见 `pd-off-block.md`，默认开启项见 `pd-on-inline.md`。
示例文字一律用英文，说明文字用中文。

## 缩写

默认关闭的原因是方括号加冒号与普通文字太像，容易误伤；开启后正文中的缩写词会带释义提示。

T:缩写定义 | 源 PM abbreviations  
预期 默认显示定义文字，开启后悬停可见释义 | 流行度 C

*[HTML]: Hyper Text Markup Language

This paragraph mentions HTML; by default the asterisk and colon stay literal.

## 硬换行

默认把段内换行合并为空格；开启 hard_line_breaks 后每一行都断开。

#### T:单行尾换行是否成为硬换行 | 源 PM hard_line_breaks | 预期 默认合并为一行，开启后每行断开

The first line has no trailing marker
the second line follows
the third line follows too

## 高亮标记

双等号在 CommonMark 中只是普通字符；开启 mark 后渲染为高亮。

T:双等号高亮 | 源 PM mark  
预期 默认显示等号原文，开启后文字带背景色 | 流行度 B

This paragraph has ==marked text== written with double equals signs.

## 标识符生成算法

默认用 Pandoc 算法；开启 gfm_auto_identifiers 后改用 GFM 算法，对中文与空格的保留程度不同。

T:标识符生成算法差异 | 源 PM gfm_auto_identifiers  
预期 默认用 Pandoc 算法，开启后改用 GFM 算法 | 流行度 C

### A heading with Chinese 中文 and English

## ASCII 标识符

开启 ascii_identifiers 后，生成的标识符只保留 ASCII 字符，非 ASCII 字符被去掉。

T:ASCII 标识符 | 源 PM ascii_identifiers  
预期 默认保留非 ASCII，开启后只留 ASCII | 流行度 D

### A heading with 中文 characters

## 忽略换行

开启 ignore_line_breaks 后，段内的换行被完全忽略、不插入空格。

#### T:忽略软换行 | 源 PM ignore_line_breaks | 预期 默认插入空格，开启后直接相连

The first line ends here
the second line continues

## 东亚换行

默认在中文之间插入空格；开启 east_asian_line_breaks 后不插入。本条对象是中文换行，保留中文。

#### T:中文之间的软换行 | 源 PM east_asian_line_breaks | 预期 默认在中文之间插入空格，开启后不插入

这一行以中文结尾，
这一行以中文开头。

## 引用链接允许空格

默认不识别方括号内含空格的引用；开启 spaced_reference_links 后不再阻碍识别。

T:方括号内含空格 | 源 PM spaced_reference_links  
预期 默认不识别，开启后成为链接 | 流行度 C

[a label with spaces][the-reference]

[the-reference]: https://example.com/ref

## 旧式破折号

默认两个短横为连接号、三个为破折号；开启 old_dashes 后两者解释互换。

T:短横的数量 | 源 PM old_dashes  
预期 默认两个短横为连接号，开启后改为三个为长破折号 | 流行度 D

In this paragraph -- is an en dash and --- is an em dash.

## 尖括号转义

默认尖括号不可转义；开启 angle_brackets_escapable 后反斜杠生效。

T:尖括号是否可被转义 | 源 PM angle_brackets_escapable  
预期 默认反斜杠无效，开启后可转义 | 流行度 D

Attempting to escape angle brackets: \<angle bracket content\>

## 单个反斜杠的数学

默认不识别；开启 tex_math_single_backslash 后成为公式。

T:反斜杠起头的公式 | 源 PM tex_math_single_backslash  
预期 默认不识别，开启后成为公式 | 流行度 C

By default the line below is just text:

\( a^2 + b^2 = c^2 \)

## 双反斜杠的数学

开启 tex_math_double_backslash 后，双反斜杠包裹的内容成为公式；与单反斜杠形式互斥。

T:双反斜杠起头的公式 | 源 PM tex_math_double_backslash  
预期 默认不识别，开启后成为公式 | 流行度 C

By default the line below is just text:

\\( a^2 + b^2 = c^2 \\)

## 相对路径重写

开启 rebase_relative_paths 后，相对路径会基于源文件位置重写。

T:相对路径重写 | 源 PM rebase_relative_paths  
预期 默认保持原样，开启后按源文件位置重写 | 流行度 D

[relative link](docs/page.md)

## 短上下标

开启 short_subsuperscripts 后，插入符或波浪线开头的短形式也可表示上下标。

T:短上下标 | 源 PM short_subsuperscripts  
预期 默认按原文，开启后成为上下标 | 流行度 C

The short forms H~2O and mc^2 appear here.

## WikiLinks（竖线后为标题）

Pandoc 的 wikilinks 扩展提供 WikiLinks，默认关闭；开启 wikilinks_title_after_pipe 后，竖线后为显示标题。

T:竖线后为标题 | 源 PM wikilinks_title_after_pipe  
预期 默认按原文，开启后成为链接 | 流行度 D

See [[Page Name|Display Title]] for details.

## WikiLinks（竖线前为标题）

开启 wikilinks_title_before_pipe 后，竖线前为显示标题，与前者互斥。

T:竖线前为标题 | 源 PM wikilinks_title_before_pipe  
预期 默认按原文，开启后成为链接 | 流行度 D

See [[Display Title|Page Name]] for details.

## 古腾堡排版

开启 gutenberg 后，按古腾堡排版约定处理引号与标点。

T:古腾堡引号 | 源 PM gutenberg  
预期 默认保持直引号，开启后按古腾堡约定替换 | 流行度 D

"Gutenberg style quotes" appear here.

## MMD 链接属性

开启 mmd_link_attributes 后，MultiMarkdown 风格的链接属性会被解析。

T:MMD 链接属性 | 源 PM mmd_link_attributes  
预期 默认显示方括号原文，开启后成为属性 | 流行度 D

[link](https://example.com)[my-id]
