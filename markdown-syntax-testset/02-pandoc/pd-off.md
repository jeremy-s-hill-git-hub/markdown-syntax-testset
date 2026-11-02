# Pandoc 默认关闭的扩展

本文件测试 Pandoc 的 `markdown` 格式下**默认不生效**的扩展。

这些语法在默认状态下按纯文本处理。
要观察其效果，需在格式名后追加 `+扩展名`，例如 `-f markdown+emoji`。

因此本文件的每一节都有两种可观察状态：**默认原样显示** 与 **开启后生效**。
示例文字一律用英文，说明文字用中文。

## 缩写

T:缩写定义 | 源 PM §abbreviations  
预期 默认显示定义文字，开启后悬停可见释义 | 流行度 C

*[HTML]: Hyper Text Markup Language

This paragraph mentions HTML; by default the asterisk and colon stay literal.

默认关闭的原因很直接：方括号加冒号这类写法与普通文字太像，容易误伤。
开启后，正文中出现的 HTML 会自动带上释义提示。

## Emoji

T:冒号包裹的短代码 | 源 PM §emoji  
预期 默认显示短代码原文，开启后渲染为图形 | 流行度 B

This paragraph has the short codes :smile: and :rocket: in it.

默认状态下它们是可见的冒号加单词。
开启后变成图形，且图形的具体样式由字体决定。

## 裸链接自动识别

T:无尖括号的网址 | 源 PM §autolink_bare_uris  
预期 默认是纯文字，开启后成为链接 | 流行度 B

By default this line is plain text: https://example.com

开启后同一行会变成可点击链接。
注意这一扩展与 GFM 的自动链接语义相近但清单不同。

## 硬换行

#### T:单行尾换行是否成为硬换行 | 源 PM §hard_line_breaks | 预期 默认合并为一行，开启后每行断开

The first line has no trailing marker
the second line follows
the third line follows too

默认状态下三行合并为一个段落，换行处变为空格。
开启后，每一行都会产生换行。
这与 CommonMark 的默认行为正好相反，也是两者最容易混淆的地方。

## 高亮标记

T:双等号高亮 | 源 PM §mark  
预期 默认显示等号原文，开启后文字带背景色 | 流行度 B

This paragraph has ==marked text== written with double equals signs.

双等号在 CommonMark 中只是普通字符。
开启后会渲染为高亮。

## 标题标识符的 GFM 风格

T:标识符生成算法差异 | 源 PM §gfm_auto_identifiers  
预期 默认用 Pandoc 算法，开启后改用 GFM 算法 | 流行度 C

### A heading with Chinese 中文 and English

上面这个标题在默认状态下会生成一种标识符。
开启后，生成规则改为 GitHub 的方式，对中文与空格的保留程度不同。

差异只在内部锚点上体现，正文外观不变。

## 东亚换行

#### T:中文之间的软换行 | 源 PM §east_asian_line_breaks | 预期 默认在中文之间插入空格，开启后不插入

这一行以中文结尾，
这一行以中文开头。

默认状态下，两行合并时中间会有一个空格，在中文语境下多余。
开启后该空格被抑制。
本条的被测量对象是中文之间的换行处理，因此保留中文。

## 四空格规则

T:列表续行的缩进判定 | 源 PM §four_space_rule  
预期 默认按标记宽度判定，开启后一律要求四空格 | 流行度 C

- The first paragraph of the item

  A continuation paragraph indented by two spaces

默认采用标记宽度判定，缩进两格即可属于同一项。
开启 `+four_space_rule` 后要求四空格，上面这段就会被判为列表之外。

## 无空行的列表

T:列表紧接段落而无需空行 | 源 PM §lists_without_preceding_blankline  
预期 默认不作为列表，开启后成为列表 | 流行度 C

The line above is a paragraph.
- By default this line does not start a list

默认要求列表前有空行。
开启该扩展后，紧贴段落的减号行也会被识别为列表。

## 引用链接允许空格

T:方括号内含空格 | 源 PM §spaced_reference_links  
预期 默认不识别，开启后成为链接 | 流行度 C

[a label with spaces][the-reference]

[the-reference]: https://example.com/ref

默认状态下这种写法不被当作引用式链接。
开启后，方括号内的空格不再阻碍识别。

## 旧式破折号

T:短横的数量 | 源 PM §old_dashes  
预期 默认两个短横为连接号，开启后改为三个为长破折号 | 流行度 D

In this paragraph -- is an en dash and --- is an em dash.

默认遵循较为现代的规则。
开启后回退到更早期的写法，两者对短横数量的解释互换。

## 尖括号转义

T:尖括号是否可被转义 | 源 PM §angle_brackets_escapable  
预期 默认反斜杠无效，开启后可转义 | 流行度 D

Attempting to escape angle brackets: \<angle bracket content\>

默认状态下尖括号不可转义，反斜杠会原样保留。
开启后反斜杠生效，尖括号变为普通字符。

## 单个反斜杠的数学

T:反斜杠起头的公式 | 源 PM §tex_math_single_backslash  
预期 默认不识别，开启后成为公式 | 流行度 C

By default the line below is just text:

\( a^2 + b^2 = c^2 \)

开启后它变为行内公式。
另有一条 `tex_math_double_backslash` 处理双反斜杠形式，两者互斥。

## 标题与块属性

T:通用属性块 | 源 PM §attributes  
预期 默认显示花括号原文，开启后被解析为属性 | 流行度 C

This line ends with an attribute block {#id .class} written literally.

`header_attributes` 只作用于标题，而 `attributes` 作用于更多位置。
两者默认状态相反，这一点容易记混。

## 小结

以上扩展在 Pandoc 的 markdown 格式下默认都不生效。

判定方式有两种：默认状态下应看到原文；追加扩展名后应看到效果。
若编辑器的结果介于两者之间，说明它实现了该语法但未完全对齐 Pandoc 规则。

默认开启的扩展见 `pd-on.md`。
