# 行内结构

本文件测试 CommonMark 的行内语法。
块级语法见 `cm-block.md`，边界与异常见 `cm-edge.md`。

示例文字一律用英文，说明文字用中文。

## 反斜杠转义

T:标点可转义 | 源 CM 0.31.2 §2.4  
预期 显示标点本身，不触发语法 | 流行度 A

\*the asterisks here are not emphasis\*

T:转义非标点字符无效 | 源 CM 0.31.2 §2.4  
预期 反斜杠原样保留 | 流行度 B

\A \a \3

T:行尾反斜杠为硬换行 | 源 CM 0.31.2 §2.4  
预期 两行之间产生换行 | 流行度 B

This line ends with a backslash\
the next line follows

T:代码跨度内转义无效 | 源 CM 0.31.2 §2.4  
预期 反斜杠原样显示 | 流行度 B

`\*no escaping inside code\*`

## 实体与字符引用

T:命名实体 | 源 CM 0.31.2 §2.5  
预期 显示为对应符号 | 流行度 A

&amp; &copy; &nbsp; &AElig;

T:十进制字符引用 | 源 CM 0.31.2 §2.5  
预期 显示为对应字符 | 流行度 B

&#35; &#1234; &#992;

T:十六进制字符引用 | 源 CM 0.31.2 §2.5  
预期 显示为对应字符 | 流行度 B

&#X22; &#x22; &#XD06;

T:非实体按原文显示 | 源 CM 0.31.2 §2.5  
预期 不解析，显示为原文 | 流行度 C

&nbsp &x; &#; &MadeUpEntity;

T:实体不能代替结构符号 | 源 CM 0.31.2 §2.5  
预期 第一行不是强调，第二行才是 | 流行度 C

&#42;foo&#42;
*foo*

T:代码跨度内实体不解析 | 源 CM 0.31.2 §2.5  
预期 显示实体原文 | 流行度 B

`&ouml; &copy;`

## 代码跨度

T:单反引号 | 源 CM 0.31.2 §6.1  
预期 等宽文字 | 流行度 A

`code`

T:双反引号包裹含反引号内容 | 源 CM 0.31.2 §6.1  
预期 显示为含反引号的代码 | 流行度 B

`` `code` ``

T:首尾空格被剥离一格 | 源 CM 0.31.2 §6.1  
预期 显示 code，前后各少一个空格 | 流行度 B

`` ` code ` ``

T:全空格代码跨度不剥离 | 源 CM 0.31.2 §6.1  
预期 空格原样保留 | 流行度 D

`` `  ` ``

T:反引号数量不等不成立 | 源 CM 0.31.2 §6.1  
预期 显示为原文 | 流行度 B

`code``

T:代码跨度内不解析任何语法 | 源 CM 0.31.2 §6.1  
预期 星号与方括号均为原文 | 流行度 A

`**not bold** [not a link](url)`

## 强调与加粗

T:星号斜体 | 源 CM 0.31.2 §6.2  
预期 斜体 | 流行度 A

*italic text*

T:星号粗体 | 源 CM 0.31.2 §6.2  
预期 粗体 | 流行度 A

**bold text**

T:下划线斜体 | 源 CM 0.31.2 §6.2  
预期 斜体 | 流行度 A

_italic text_

T:下划线粗体 | 源 CM 0.31.2 §6.2  
预期 粗体 | 流行度 A

__bold text__

T:三星号粗斜体 | 源 CM 0.31.2 §6.2  
预期 粗体加斜体 | 流行度 A

***bold and italic text***

T:嵌套：粗体内含斜体 | 源 CM 0.31.2 §6.2  
预期 粗体内局部斜体 | 流行度 B

**bold with *italic* inside**

T:词内下划线不触发 | 源 CM 0.31.2 §6.2  
预期 显示为原文，不斜体 | 流行度 B

snake_case_name_and_more

T:词内星号可触发 | 源 CM 0.31.2 §6.2  
预期 中间部分斜体 | 流行度 B

foo*bar*baz

T:左右均为空白的定界符不成立 | 源 CM 0.31.2 §6.2  
预期 显示为原文 | 流行度 C

a * b * c

T:不匹配长度定界符 | 源 CM 0.31.2 §6.2  
预期 多余星号显示在强调之外 | 流行度 C

**foo*

T:转义可阻止强调 | 源 CM 0.31.2 §6.2  
预期 全部为原文 | 流行度 B

\*not italic\*

## 链接

T:行内链接 | 源 CM 0.31.2 §6.3  
预期 可点击链接 | 流行度 A

[inline link](https://example.com)

T:带标题的行内链接 | 源 CM 0.31.2 §6.3  
预期 悬停显示标题 | 流行度 A

[link with title](https://example.com "Hover to see this title")

T:标题可用单引号或括号 | 源 CM 0.31.2 §6.3  
预期 两种写法都生成标题 | 流行度 B

[single quoted title](https://example.com 'single')

[parenthesised title](https://example.com (paren))

T:尖括号包裹目标 | 源 CM 0.31.2 §6.3  
预期 可点击链接，目标含空格也可 | 流行度 B

[angle bracket destination](<https://example.com/a b>)

T:空目标 | 源 CM 0.31.2 §6.3  
预期 可点击但目标为空 | 流行度 C

[empty destination]()

T:引用式完整写法 | 源 CM 0.31.2 §6.3  
预期 可点击链接 | 流行度 A

[full reference form][ci-ref-1]

[ci-ref-1]: https://example.com/ref1 "Reference title"

T:引用式简写 | 源 CM 0.31.2 §6.3  
预期 可点击链接 | 流行度 B

[ci-ref-2]

[ci-ref-2]: https://example.com/ref2

T:引用标签大小写不敏感 | 源 CM 0.31.2 §6.3  
预期 可点击链接 | 流行度 B

[CI-REF-3]

[ci-ref-3]: https://example.com/ref3

T:链接文字可含行内语法 | 源 CM 0.31.2 §6.3  
预期 链接内的字为粗体 | 流行度 B

[link with **bold** text](https://example.com)

T:链接不可嵌套 | 源 CM 0.31.2 §6.3  
预期 内层成为链接，外层为原文 | 流行度 C

[outer [inner](https://example.com/inner)](https://example.com/outer)

T:未定义引用按原文显示 | 源 CM 0.31.2 §6.3  
预期 显示方括号原文 | 流行度 B

[missing][ci-ref-none]

T:指向本文档锚点 | 源 CM 0.31.2 §6.3  
预期 点击跳转到本文件锚点 | 流行度 A

[jump to code spans](#代码跨度)

## 图片

T:基本图片 | 源 CM 0.31.2 §6.4  
预期 显示图片，失败则显示替代文字 | 流行度 A

![alt text](media/placeholder.svg "Image title")

T:图片可含行内语法于替代文字 | 源 CM 0.31.2 §6.4  
预期 替代文字中的粗体在加载失败时可辨 | 流行度 C

![alt text with **bold**](media/placeholder.svg)

T:引用式图片 | 源 CM 0.31.2 §6.4  
预期 显示图片 | 流行度 B

![reference image][ci-img-1]

[ci-img-1]: media/placeholder.svg

## 自动链接

T:URI 自动链接 | 源 CM 0.31.2 §6.5  
预期 显示为可点击链接，文字即网址 | 流行度 A

<https://example.com/auto>

T:邮件自动链接 | 源 CM 0.31.2 §6.5  
预期 显示为可点击邮件链接 | 流行度 A

<mail@example.com>

T:非绝对 URI 不成立 | 源 CM 0.31.2 §6.5  
预期 显示为原文尖括号 | 流行度 C

<not a uri>

## 原始 HTML

T:行内标签 | 源 CM 0.31.2 §6.6  
预期 渲染为对应效果 | 流行度 A

Press <kbd>Ctrl</kbd> plus <kbd>C</kbd> to copy.

T:行内换行标签 | 源 CM 0.31.2 §6.6  
预期 该处产生换行 | 流行度 B

First line<br>second line

T:带属性的行内标签 | 源 CM 0.31.2 §6.6  
预期 文字显示为红色 | 流行度 B

<span style="color: #c00;">red text</span>

T:自定义标签名 | 源 CM 0.31.2 §6.6  
预期 标签被当作原始 HTML 输出，可能不产生视觉效果 | 流行度 C

<my-custom>custom tag content</my-custom>

T:尖括号内的非标签按原文处理 | 源 CM 0.31.2 §6.6  
预期 显示为原文，或被当作 HTML 转义 | 流行度 B

a < b and c > d

## 硬换行

#### T:行尾两个空格产生换行 | 源 CM 0.31.2 §6.7 | 预期 两行在同段内但换行显示

The first line ends with two spaces  
the second line follows immediately

#### T:行尾反斜杠产生换行 | 源 CM 0.31.2 §6.7 | 预期 两行在同段内但换行显示

The first line ends with a backslash\
the second line follows immediately

#### T:行尾无标记时合并为一行 | 源 CM 0.31.2 §6.7 | 预期 两行合并为连续文字，换行与否取决于渲染宽度

The first line has no trailing marker
the second line follows immediately

#### T:代码块内行尾空格不产生换行 | 源 CM 0.31.2 §6.7 | 预期 代码块内两行各自独立

The code block below has trailing spaces that do not create a line break

```
first line  
second line
```

## 软换行

#### T:软换行转换为空格或换行 | 源 CM 0.31.2 §6.8 | 预期 两行之间通常渲染为一个空格，也可渲染为换行

The first line of a soft break
the second line of a soft break

## 文本内容

#### T:普通文字原样输出 | 源 CM 0.31.2 §6.9 | 预期 文字内容不变，仅做 HTML 转义

Plain text with < and & is escaped but still displays the same

## 未闭合

以下用例故意保持未闭合，全部位于文件末尾，防止吞噬后续内容。

T:未闭合自动链接 | 源 CM 0.31.2 §6.5  
预期 尖括号按原文显示，不吞掉后续文字 | 流行度 C

Here is an <https://example.com without the closing angle bracket.

T:未闭合代码跨度不跨空行 | 源 CM 0.31.2 §6.1  
预期 两段的反引号都按原文显示，不跨段配对 | 流行度 C

Here is an `unclosed span

and a second lone backtick `

T:未闭合定界符当原文 | 源 CM 0.31.2 §6.2  
预期 星号原样显示 | 流行度 C

**unclosed bold
