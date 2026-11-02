# 边界与异常

本文件测试 CommonMark 在异常、临界、未闭合输入下的行为。
块级语法见 `cm-block.md`，行内语法见 `cm-inline.md`，未闭合用例集中在文件末尾。

示例文字一律用英文，说明文字用中文。
例外：被测量对象本身是中文的用例（全角标点、全角空格、东亚换行）必须保留中文，否则测不到。

## 缩进临界

T:三空格不构成代码块 | 源 CM 0.31.2 §4.4  
预期 显示为段落 | 流行度 B

   A paragraph indented by three spaces

T:四空格构成代码块 | 源 CM 0.31.2 §4.4  
预期 显示为代码块 | 流行度 A

    A code block indented by four spaces

T:制表符等同四空格 | 源 CM 0.31.2 §2.2  
预期 显示为代码块 | 流行度 B

	tab indented code

T:列表项内缩进以标记宽度为基准 | 源 CM 0.31.2 §5.2  
预期 两段同属列表项 | 流行度 B

- The first paragraph of this item

  The second paragraph, indented by two spaces

T:引用内代码块需五空格 | 源 CM 0.31.2 §5.1  
预期 引用内出现代码块 | 流行度 C

>     A code block inside a block quote, five spaces after the marker

## 空输入与空块

T:空文档 | 源 CM 0.31.2 §1  
预期 本节不产生任何可见内容，不报错 | 流行度 B

T:只有空行的文档 | 源 CM 0.31.2 §4.9  
预期 本节不产生任何可见内容，不报错 | 流行度 C

T:空引用块 | 源 CM 0.31.2 §5.1  
预期 渲染为空引用块或不可见 | 流行度 C

>

T:空列表项 | 源 CM 0.31.2 §5.2  
预期 渲染为含空项与两个有内容项的列表 | 流行度 C

- Item with content
-
- Item with content

T:空标题 | 源 CM 0.31.2 §4.2  
预期 渲染为标题但无文字 | 流行度 D

##

## Unicode 与特殊字符

T:中文与全角标点 | 源 CM 0.31.2 §2.1  
预期 原样显示 | 流行度 A

中文，全角逗号、句号。还有「引号」和『书名号』。

T:emoji 与组合符号 | 源 CM 0.31.2 §2.1  
预期 原样显示 | 流行度 B

😀 👍🏽 👨‍👩‍👧‍👦 é

T:从右到左文字 | 源 CM 0.31.2 §2.1  
预期 正常显示，方向由编辑器决定 | 流行度 C

مرحبا שלום

T:零宽字符与不换行空格 | 源 CM 0.31.2 §2.1  
预期 不可见或显示为极窄空白 | 流行度 D

a​b c

T:反引号与星号在中文语境 | 源 CM 0.31.2 §6.2  
预期 粗体与代码正常生效 | 流行度 B

**中文粗体**与`中文代码`

T:全角空格不等同于半角空格 | 源 CM 0.31.2 §2.1  
预期 缩进无效，显示为段落 | 流行度 D

　　全角空格开头的段落

## 超长与深层嵌套

T:超长单行 | 源 CM 0.31.2 §2.1  
预期 正常换行显示，不截断 | 流行度 C

This line is deliberately very long, used to observe how the editor wraps and scrolls a single extremely long line. The content itself is meaningless; it exists only to build up enough length, filling and filling and filling and filling and filling and filling and filling and filling and filling and filling and filling and filling and filling and filling until the line is long enough. End of line.

T:深层嵌套引用 | 源 CM 0.31.2 §5.1  
预期 呈现多层引用缩进 | 流行度 C

> > > > > Five levels of nested block quotes

T:深层嵌套列表 | 源 CM 0.31.2 §5.3  
预期 呈现多层列表缩进 | 流行度 C

- Level one
  - Level two
    - Level three
      - Level four
        - Level five

T:列表内代码块 | 源 CM 0.31.2 §5.2  
预期 代码块属于列表项 | 流行度 B

1. A list item

   ```
   a fenced code block inside the list item
   ```

T:引用内列表 | 源 CM 0.31.2 §5.1  
预期 引用内出现列表 | 流行度 B

> - The first item inside a quote
> - The second item inside a quote

T:列表内引用 | 源 CM 0.31.2 §5.2  
预期 列表项内出现引用 | 流行度 B

- A list item

  > A block quote inside the list item

## 行尾与换行符

#### T:行尾一个空格不产生换行 | 源 CM 0.31.2 §6.7 | 预期 两行合并为一段，不换行

The first line ends with a single space 
the second line follows

#### T:行尾三个及以上空格产生换行 | 源 CM 0.31.2 §6.7 | 预期 两行之间产生换行

The first line ends with three spaces   
the second line follows

#### T:段落末尾的空格被剥离 | 源 CM 0.31.2 §4.8 | 预期 段尾不产生多余换行

This paragraph ends with two spaces  

#### T:制表符在行尾不产生换行 | 源 CM 0.31.2 §2.2 | 预期 两行合并，不产生硬换行

The first line ends with a tab	
the second line follows

## 围栏异常

T:三反引号围栏 | 源 CM 0.31.2 §4.5  
预期 代码块，内容不被解析 | 流行度 A

```
fenced code block content
**the asterisks here should not become bold**
```

T:五反引号围栏可含三反引号 | 源 CM 0.31.2 §4.5  
预期 代码块内出现三反引号原文 | 流行度 B

`````
```
nested triple backticks
```
`````

T:波浪线不能闭合反引号围栏 | 源 CM 0.31.2 §4.5  
预期 中间的波浪线是代码内容，不是闭合符 | 流行度 C

```
a tilde line cannot close a backtick fence
~~~
this line is still inside the code block
```

## 未闭合语法

以下用例故意保持未闭合，用于观察内容是否被吞掉。

T:未闭合星号强调 | 源 CM 0.31.2 §6.2  
预期 星号按原文显示，不吞掉后续文字 | 流行度 C

Here is an **unclosed bold marker and the text after it should still be visible.

T:未闭合下划线强调 | 源 CM 0.31.2 §6.2  
预期 下划线按原文显示 | 流行度 C

Here is an __unclosed underscore bold and the text after it should still be visible.

T:未闭合代码跨度 | 源 CM 0.31.2 §6.1  
预期 反引号按原文显示 | 流行度 C

Here is an `unclosed code span and the text after it should still be visible.

T:未闭合链接方括号 | 源 CM 0.31.2 §6.3  
预期 方括号按原文显示 | 流行度 C

Here is an [unclosed link text and the text after it should still be visible.

T:未闭合链接圆括号 | 源 CM 0.31.2 §6.3  
预期 整体按原文显示 | 流行度 C

Here is a [link with text](unclosed destination

T:未闭合图片 | 源 CM 0.31.2 §6.4  
预期 整体按原文显示 | 流行度 C

Here is an ![unclosed image](media/placeholder.svg

T:未闭合 HTML 标签 | 源 CM 0.31.2 §6.6  
预期 按原文显示或被忽略 | 流行度 C

Here is an <span unclosed tag

T:未闭合围栏吞掉余下内容 | 源 CM 0.31.2 §4.5  
预期 本行之后到文件末尾全部成为代码 | 流行度 B

~~~text
If no closing fence appears, everything after this line becomes code.
This is the last block of this file, used to observe the extent of an unclosed fence.
