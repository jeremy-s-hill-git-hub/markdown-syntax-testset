# 块级结构

本文件测试 CommonMark 的块级语法。
行内语法见 `cm-inline.md`，边界与异常见 `cm-edge.md`。

示例文字一律用英文，说明文字用中文。

## 分隔线

分隔线是一行水平分割线：最多三格缩进后，接三个及以上同一种字符（`*`、`-` 或 `_`），字符之间可夹空格或制表符，行内不得出现其他字符。少于三个或混用字符都不成立——规范要求"三个及以上且同种"，是为了与列表标记（`-`）和强调（`*`）等短构造区分，避免同一行在不同上下文中产生歧义。

T:三种分隔线 | 源 CM 0.31.2 第 4.1 节  
预期 三条水平线 | 流行度 A

***

---

___

T:字符间允许空格 | 源 CM 0.31.2 第 4.1 节  
预期 一条水平线 | 流行度 B

- - -

T:缩进一至三格仍成立 | 源 CM 0.31.2 第 4.1 节  
预期 一条水平线 | 流行度 B

 ***

T:缩进四格为代码块 | 源 CM 0.31.2 第 4.1 节  
预期 不是水平线，而是代码块 | 流行度 B

    ***

T:不足三个字符不成立 | 源 CM 0.31.2 第 4.1 节  
预期 显示为原文 | 流行度 B

--

T:混用字符不成立 | 源 CM 0.31.2 第 4.1 节  
预期 渲染为斜体连字符 | 流行度 C

*-*

## ATX 标题

ATX 标题以一到六个井号开头，后接空格与标题文字；可带任意数量的收尾井号，收尾井号不计入标题文字。七个及以上井号不构成标题（超出六级上限）；井号后没有空格也不构成标题，以便与话题标签（如 `#hashtag`）区分。

T:一至六级标题 | 源 CM 0.31.2 第 4.2 节  
预期 六个不同级别的标题 | 流行度 A

# Level one heading

## Level two heading

### Level three heading

#### Level four heading

##### Level five heading

###### Level six heading

T:七个井号不是标题 | 源 CM 0.31.2 第 4.2 节  
预期 显示为段落原文 | 流行度 B

####### Seven hashes is not a heading

T:井号后必须有空格 | 源 CM 0.31.2 第 4.2 节  
预期 显示为段落原文 | 流行度 B

#hashtag

T:可带收尾井号 | 源 CM 0.31.2 第 4.2 节  
预期 标题文字不含井号 | 流行度 B

## Heading with closing hashes ##

T:转义井号不构成标题 | 源 CM 0.31.2 第 4.2 节  
预期 显示为段落原文 | 流行度 C

\## Escaped hash is not a heading

## Setext 标题

Setext 标题由一行文字加下一行下划线构成：等号为一级，连字符为二级，下划线可重复；标题文字可跨多行。下划线行全是连字符时也可解释为分隔线，规范规定此时优先组成标题。

T:等号下划线为一级 | 源 CM 0.31.2 第 4.3 节  
预期 一级标题 | 流行度 A

Setext level one
================

T:连字符下划线为二级 | 源 CM 0.31.2 第 4.3 节  
预期 二级标题 | 流行度 A

Setext level two
----------------

T:内容可跨行 | 源 CM 0.31.2 第 4.3 节  
预期 一个标题，文字跨两行 | 流行度 B

This heading spans
two lines
====

T:分隔线与 Setext 的取舍 | 源 CM 0.31.2 第 4.3 节  
预期 上两行组成二级标题 | 流行度 B

Setext wins over thematic break
---

## 缩进代码块

缩进代码块由四空格缩进（或一个制表符）开始，缩进不属于代码内容，内容原样保留、不解析行内语法。它不能打断段落：若前面段落尚未结束，缩进四格的行仍属于该段落。

T:四空格缩进 | 源 CM 0.31.2 第 4.4 节  
预期 等宽代码块，缩进被去掉 | 流行度 A

    a simple
      indented code block

T:制表符等同四空格 | 源 CM 0.31.2 第 4.4 节  
预期 代码块 | 流行度 B

	tab indented code

T:不能打断段落 | 源 CM 0.31.2 第 4.4 节  
预期 全部为同一段落，不形成代码块 | 流行度 C

First line of a paragraph
    this line is indented four spaces but still belongs to the paragraph

## HTML 块

块级 HTML 原样输出，交由浏览器解析渲染，行内样式同样生效；HTML 注释不会显示。CommonMark 在 HTML 块内部不解析 Markdown，HTML 与 Markdown 的边界由块级标签决定。

T:块级 HTML 直通 | 源 CM 0.31.2 第 4.6 节  
预期 渲染为实际元素 | 流行度 B

<div>A block level div element</div>

T:行内样式在块内生效 | 源 CM 0.31.2 第 4.6 节  
预期 红色文字 | 流行度 C

<p style="color: #c00;">A paragraph with an inline style</p>

T:注释不显示 | 源 CM 0.31.2 第 4.6 节  
预期 页面上看不到任何文字 | 流行度 B

<!-- This comment should not appear in the rendered output -->

## 链接引用定义

链接引用定义形如 `[标签]: 目标 "标题"`，可放在文档任意位置，甚至先于引用出现。未定义的引用按原文显示；目标为空的定义无效。

T:引用式链接 | 源 CM 0.31.2 第 4.7 节  
预期 显示为可点击链接，文字为 reference link | 流行度 A

[reference link][ref-a]

[ref-a]: https://example.com "Reference title"

T:引用可先于定义出现 | 源 CM 0.31.2 第 4.7 节  
预期 正常渲染为链接 | 流行度 B

[ref-b]

[ref-b]: https://example.com/b

T:未定义的引用不渲染 | 源 CM 0.31.2 第 4.7 节  
预期 显示为原文方括号 | 流行度 B

[undefined reference][ref-not-exist]

T:引用定义目标为空 | 源 CM 0.31.2 第 4.7 节  
预期 定义无效，引用按原文显示 | 流行度 C

[empty destination][ref-empty]

[ref-empty]:

## 段落

段落是一行或多行连续文字，行间没有空行时合并为同一段，换行按空格处理。段落首行最多缩进三格仍是段落；连续多个空行的效果与一个空行相同。

#### T:空行分段 | 源 CM 0.31.2 第 4.8 节 | 预期 两个独立段落

The first paragraph.

The second paragraph.

#### T:无空行则续行 | 源 CM 0.31.2 第 4.8 节 | 预期 三行合并为一个段落

This line and the next one
have no blank line between them,
so they form a single paragraph.

#### T:段落首行最多缩进三格 | 源 CM 0.31.2 第 4.8 节 | 预期 仍然是一个段落，不是代码块

   Three spaces of indentation still make a paragraph
the second line follows

#### T:连续多个空行无影响 | 源 CM 0.31.2 第 4.8 节 | 预期 两个段落，间距与一个空行相同

First paragraph.



Second paragraph.

## 空行

空行用于分隔块级元素。文档首尾的空行被忽略；列表项之间是否插入空行，决定列表是紧凑还是松散。

#### T:文档首尾空行被忽略 | 源 CM 0.31.2 第 4.9 节 | 预期 渲染结果不含多余空白

This paragraph has extra blank lines before and after it.

#### T:空行决定列表紧凑程度 | 源 CM 0.31.2 第 4.9 节 | 预期 上一个列表紧凑，下一个列表松散

- Tight item one
- Tight item two

- Loose item one

- Loose item two

## 引用块

引用块以大于号加可选空格开头，可包含标题、段落、列表等其他块级元素。每行的大于号可省略（惰性续行），但空行会结束当前引用；引用可以嵌套。

T:基本引用 | 源 CM 0.31.2 第 5.1 节  
预期 渲染为引用块 | 流行度 A

> A single paragraph inside a block quote.

T:引用内可含其他块 | 源 CM 0.31.2 第 5.1 节  
预期 引用块内出现标题与段落 | 流行度 B

> ## A heading inside a quote
>
> A paragraph inside the same quote.

T:省略大于号仍属引用 | 源 CM 0.31.2 第 5.1 节  
预期 两行同属一个引用块 | 流行度 B

> This line starts with a greater than sign
and this line omits it but is still inside the quote

T:空行分隔两个引用 | 源 CM 0.31.2 第 5.1 节  
预期 两个独立引用块 | 流行度 B

> The first block quote

> The second block quote

T:嵌套引用 | 源 CM 0.31.2 第 5.1 节  
预期 呈现多层引用 | 流行度 C

> Outer level
>
> > Inner level
>
> Back to outer level

## 列表项

无序列表用连字符、加号或星号作标记；有序列表用点号或右括号收尾，起始编号由标记决定。列表项可包含多个块；标记与内容之间必须有空格，否则按段落原文处理。

T:无序列表三种标记 | 源 CM 0.31.2 第 5.2 节  
预期 三个独立列表，各自渲染 | 流行度 A

- Hyphen item

+ Plus item

* Asterisk item

T:有序列表两种收尾 | 源 CM 0.31.2 第 5.2 节  
预期 两个独立的有序列表 | 流行度 A

1. Period item one
2. Period item two

1) Paren item one
2) Paren item two

T:有序列表起始编号 | 源 CM 0.31.2 第 5.2 节  
预期 编号从 5 开始 | 流行度 B

5. The fifth item
6. The sixth item

T:列表项可含多个块 | 源 CM 0.31.2 第 5.2 节  
预期 一项内含段落与引用 | 流行度 B

1. The first paragraph of this item

   A second paragraph of the same item

   > A block quote inside the same item

T:标记与内容之间需空格 | 源 CM 0.31.2 第 5.2 节  
预期 显示为段落原文 | 流行度 C

-no space means no list

## 列表

列表项之间有空行则为松散列表（项内包段落），无空行则为紧凑列表；嵌套靠缩进实现；标记类型变化（如编号改为符号）会另起一个列表；列表可以打断段落。

T:紧凑列表 | 源 CM 0.31.2 第 5.3 节  
预期 项内不包段落 | 流行度 A

- Item one
- Item two
- Item three

T:松散列表 | 源 CM 0.31.2 第 5.3 节  
预期 项内包裹段落，间距变大 | 流行度 A

- Item one

- Item two

T:嵌套列表 | 源 CM 0.31.2 第 5.3 节  
预期 三层嵌套 | 流行度 A

- First level
  - Second level
    - Third level

T:标记类型变化即另起列表 | 源 CM 0.31.2 第 5.3 节  
预期 一个列表内编号与符号混合 | 流行度 C

1. Numbered item
2. Numbered item
- Bullet item
- Bullet item

T:列表可打断段落 | 源 CM 0.31.2 第 5.3 节  
预期 上一行成段落，其后为列表 | 流行度 B

This line is a paragraph.
- A list item follows immediately

## 未闭合与围栏

围栏代码块用三个及以上反引号或波浪线起止，内容不解析行内语法；起始围栏可带语言标记，收尾围栏长度不得短于起始。以下故意保留未闭合构造，按吞噬范围递增排列，用于观察编辑器在异常输入下的表现。

T:反引号围栏代码块 | 源 CM 0.31.2 第 4.5 节  
预期 等宽代码块，内容不被解析 | 流行度 A

```
fenced code block
**the asterisks here should not become bold**
```

T:波浪线围栏 | 源 CM 0.31.2 第 4.5 节  
预期 等宽代码块 | 流行度 B

~~~
tilde fenced block
~~~

T:带语言标记的围栏 | 源 CM 0.31.2 第 4.5 节  
预期 代码块带语言标记，可能触发高亮 | 流行度 A

```python
def hello():
    return "world"
```

T:围栏长度可增 | 源 CM 0.31.2 第 4.5 节  
预期 四反引号围栏，内部可含三反引号 | 流行度 B

````
```
nested triple backticks
```
````

T:未闭合强调 | 源 CM 0.31.2 第 6.2 节  
预期 星号按原文显示，不吞掉后续内容 | 流行度 C

Here is an unclosed **emphasis marker and the text after it

T:未闭合的方括号 | 源 CM 0.31.2 第 6.3 节  
预期 方括号按原文显示 | 流行度 C

Here is an unclosed [bracket and the text after it

T:未闭合围栏吞掉文件余下内容 | 源 CM 0.31.2 第 4.5 节  
预期 本行之后到文件末尾全部成为代码 | 流行度 B

```text
If no closing fence appears, everything after this line becomes code.
This is the last block of this file, used to observe the extent of an unclosed fence.
