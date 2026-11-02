# 吞噬型未闭合构造

本文件测试「一旦出现就覆盖其后全部内容」的未闭合构造。

这类构造有一个结构性限制：只要它出现，其后的内容都不再被解析，因此**一个文件只能容纳一条**。本文件把不吞噬的对照用例放在前面，把唯一一条吞噬用例放在文件最末。

示例文字一律用英文，说明文字用中文。

## 对照：未闭合块级标签由空行终止

T:未闭合 div 由空行终止 | 源 CM 0.31.2 §4.6  
预期 div 内文字仍可见，其后段落正常渲染 | 流行度 B

<div>
This paragraph is inside an unterminated div element.

This paragraph comes after a blank line and should render normally, outside the div.

## 对照：未闭合行内标签不吞噬

T:未闭合行内标签按原文 | 源 CM 0.31.2 §6.6  
预期 尖括号按原文显示，段落其余部分正常 | 流行度 C

Press <kbd to see how an unterminated inline tag behaves.

## 吞噬：未闭合 HTML 注释

T:未闭合 HTML 注释吞到文件末尾 | 源 CM 0.31.2 §4.6  
预期 本标签之后到文件末尾全部不显示 | 流行度 B

<!--
Everything from the line above to the end of this file belongs to the comment and must not be rendered.
