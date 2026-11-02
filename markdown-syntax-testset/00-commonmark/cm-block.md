# 块级结构

本文件测试 CommonMark 的块级语法。
行内语法见 `cm-inline.md`，边界与异常见 `cm-edge.md`。

示例文字一律用英文，说明文字用中文。

## 分隔线

T:三种分隔线 | 源 CM 0.31.2 §4.1  
预期 三条水平线 | 流行度 A

***

---

___

T:字符间允许空格 | 源 CM 0.31.2 §4.1  
预期 一条水平线 | 流行度 B

- - -

T:缩进一至三格仍成立 | 源 CM 0.31.2 §4.1  
预期 一条水平线 | 流行度 B

 ***

T:缩进四格为代码块 | 源 CM 0.31.2 §4.1  
预期 不是水平线，而是代码块 | 流行度 B

    ***

T:不足三个字符不成立 | 源 CM 0.31.2 §4.1  
预期 显示为原文 | 流行度 B

--

T:混用字符不成立 | 源 CM 0.31.2 §4.1  
预期 渲染为斜体连字符 | 流行度 C

*-*

## ATX 标题

T:一至六级标题 | 源 CM 0.31.2 §4.2  
预期 六个不同级别的标题 | 流行度 A

# Level one heading

## Level two heading

### Level three heading

#### Level four heading

##### Level five heading

###### Level six heading

T:七个井号不是标题 | 源 CM 0.31.2 §4.2  
预期 显示为段落原文 | 流行度 B

####### Seven hashes is not a heading

T:井号后必须有空格 | 源 CM 0.31.2 §4.2  
预期 显示为段落原文 | 流行度 B

#hashtag

T:可带收尾井号 | 源 CM 0.31.2 §4.2  
预期 标题文字不含井号 | 流行度 B

## Heading with closing hashes ##

T:转义井号不构成标题 | 源 CM 0.31.2 §4.2  
预期 显示为段落原文 | 流行度 C

\## Escaped hash is not a heading

## Setext 标题

T:等号下划线为一级 | 源 CM 0.31.2 §4.3  
预期 一级标题 | 流行度 A

Setext level one
================

T:连字符下划线为二级 | 源 CM 0.31.2 §4.3  
预期 二级标题 | 流行度 A

Setext level two
----------------

T:内容可跨行 | 源 CM 0.31.2 §4.3  
预期 一个标题，文字跨两行 | 流行度 B

This heading spans
two lines
====

T:分隔线与 Setext 的取舍 | 源 CM 0.31.2 §4.3  
预期 上两行组成二级标题 | 流行度 B

Setext wins over thematic break
---

## 缩进代码块

T:四空格缩进 | 源 CM 0.31.2 §4.4  
预期 等宽代码块，缩进被去掉 | 流行度 A

    a simple
      indented code block

T:制表符等同四空格 | 源 CM 0.31.2 §4.4  
预期 代码块 | 流行度 B

	tab indented code

T:不能打断段落 | 源 CM 0.31.2 §4.4  
预期 全部为同一段落，不形成代码块 | 流行度 C

First line of a paragraph
    this line is indented four spaces but still belongs to the paragraph

## HTML 块

T:块级 HTML 直通 | 源 CM 0.31.2 §4.6  
预期 渲染为实际元素 | 流行度 B

<div>A block level div element</div>

T:行内样式在块内生效 | 源 CM 0.31.2 §4.6  
预期 红色文字 | 流行度 C

<p style="color: #c00;">A paragraph with an inline style</p>

T:注释不显示 | 源 CM 0.31.2 §4.6  
预期 页面上看不到任何文字 | 流行度 B

<!-- This comment should not appear in the rendered output -->

## 链接引用定义

T:引用式链接 | 源 CM 0.31.2 §4.7  
预期 显示为可点击链接，文字为 reference link | 流行度 A

[reference link][ref-a]

[ref-a]: https://example.com "Reference title"

T:引用可先于定义出现 | 源 CM 0.31.2 §4.7  
预期 正常渲染为链接 | 流行度 B

[ref-b]

[ref-b]: https://example.com/b

T:未定义的引用不渲染 | 源 CM 0.31.2 §4.7  
预期 显示为原文方括号 | 流行度 B

[undefined reference][ref-not-exist]

T:引用定义目标为空 | 源 CM 0.31.2 §4.7  
预期 定义无效，引用按原文显示 | 流行度 C

[empty destination][ref-empty]

[ref-empty]:

## 段落

#### T:空行分段 | 源 CM 0.31.2 §4.8 | 预期 两个独立段落

The first paragraph.

The second paragraph.

#### T:无空行则续行 | 源 CM 0.31.2 §4.8 | 预期 三行合并为一个段落

This line and the next one
have no blank line between them,
so they form a single paragraph.

#### T:段落首行最多缩进三格 | 源 CM 0.31.2 §4.8 | 预期 仍然是一个段落，不是代码块

   Three spaces of indentation still make a paragraph
the second line follows

#### T:连续多个空行无影响 | 源 CM 0.31.2 §4.8 | 预期 两个段落，间距与一个空行相同

First paragraph.



Second paragraph.

## 空行

#### T:文档首尾空行被忽略 | 源 CM 0.31.2 §4.9 | 预期 渲染结果不含多余空白

This paragraph has extra blank lines before and after it.

#### T:空行决定列表紧凑程度 | 源 CM 0.31.2 §4.9 | 预期 上一个列表紧凑，下一个列表松散

- Tight item one
- Tight item two

- Loose item one

- Loose item two

## 引用块

T:基本引用 | 源 CM 0.31.2 §5.1  
预期 渲染为引用块 | 流行度 A

> A single paragraph inside a block quote.

T:引用内可含其他块 | 源 CM 0.31.2 §5.1  
预期 引用块内出现标题与段落 | 流行度 B

> ## A heading inside a quote
>
> A paragraph inside the same quote.

T:省略大于号仍属引用 | 源 CM 0.31.2 §5.1  
预期 两行同属一个引用块 | 流行度 B

> This line starts with a greater than sign
and this line omits it but is still inside the quote

T:空行分隔两个引用 | 源 CM 0.31.2 §5.1  
预期 两个独立引用块 | 流行度 B

> The first block quote

> The second block quote

T:嵌套引用 | 源 CM 0.31.2 §5.1  
预期 呈现多层引用 | 流行度 C

> Outer level
>
> > Inner level
>
> Back to outer level

## 列表项

T:无序列表三种标记 | 源 CM 0.31.2 §5.2  
预期 三个独立列表，各自渲染 | 流行度 A

- Hyphen item

+ Plus item

* Asterisk item

T:有序列表两种收尾 | 源 CM 0.31.2 §5.2  
预期 两个独立的有序列表 | 流行度 A

1. Period item one
2. Period item two

1) Paren item one
2) Paren item two

T:有序列表起始编号 | 源 CM 0.31.2 §5.2  
预期 编号从 5 开始 | 流行度 B

5. The fifth item
6. The sixth item

T:列表项可含多个块 | 源 CM 0.31.2 §5.2  
预期 一项内含段落与引用 | 流行度 B

1. The first paragraph of this item

   A second paragraph of the same item

   > A block quote inside the same item

T:标记与内容之间需空格 | 源 CM 0.31.2 §5.2  
预期 显示为段落原文 | 流行度 C

-no space means no list

## 列表

T:紧凑列表 | 源 CM 0.31.2 §5.3  
预期 项内不包段落 | 流行度 A

- Item one
- Item two
- Item three

T:松散列表 | 源 CM 0.31.2 §5.3  
预期 项内包裹段落，间距变大 | 流行度 A

- Item one

- Item two

T:嵌套列表 | 源 CM 0.31.2 §5.3  
预期 三层嵌套 | 流行度 A

- First level
  - Second level
    - Third level

T:标记类型变化即另起列表 | 源 CM 0.31.2 §5.3  
预期 一个列表内编号与符号混合 | 流行度 C

1. Numbered item
2. Numbered item
- Bullet item
- Bullet item

T:列表可打断段落 | 源 CM 0.31.2 §5.3  
预期 上一行成段落，其后为列表 | 流行度 B

This line is a paragraph.
- A list item follows immediately

## 未闭合与围栏

以下语法故意保持未闭合，用于观察编辑器在异常输入下的表现。

T:反引号围栏代码块 | 源 CM 0.31.2 §4.5  
预期 等宽代码块，内容不被解析 | 流行度 A

```
fenced code block
**the asterisks here should not become bold**
```

T:波浪线围栏 | 源 CM 0.31.2 §4.5  
预期 等宽代码块 | 流行度 B

~~~
tilde fenced block
~~~

T:带语言标记的围栏 | 源 CM 0.31.2 §4.5  
预期 代码块带语言标记，可能触发高亮 | 流行度 A

```python
def hello():
    return "world"
```

T:围栏长度可增 | 源 CM 0.31.2 §4.5  
预期 四反引号围栏，内部可含三反引号 | 流行度 B

````
```
nested triple backticks
```
````

T:未闭合强调 | 源 CM 0.31.2 §6.2  
预期 星号按原文显示，不吞掉后续内容 | 流行度 C

Here is an unclosed **emphasis marker and the text after it

T:未闭合的方括号 | 源 CM 0.31.2 §6.3  
预期 方括号按原文显示 | 流行度 C

Here is an unclosed [bracket and the text after it

T:未闭合围栏吞掉文件余下内容 | 源 CM 0.31.2 §4.5  
预期 本行之后到文件末尾全部成为代码 | 流行度 B

```text
If no closing fence appears, everything after this line becomes code.
This is the last block of this file, used to observe the extent of an unclosed fence.
