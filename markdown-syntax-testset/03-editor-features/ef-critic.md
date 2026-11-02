# CriticMarkup 修订标记

本文件测试 CriticMarkup 的修订标记。它用花括号包裹，与被测内容不冲突。
被测对象是编辑器是否识别标记并渲染为修订样式，未支持时应原样显示。
示例文字一律用英文，说明文字用中文。
注：Pandoc 的高亮 `==text==`（见 `pd-off-inline.md` 的 T:双等号高亮）不含花括号，与本文件的高亮形态不同，另见本文 T:三种定界符对照。

CriticMarkup 用花括号包裹修订标记：插入、删除、替换、高亮、注释各有定界符。它不是 Markdown 规范语法，未支持时按原文显示；因为定界符是花括号，与星号、波浪线等常见定界符不冲突，所以可以和它们共存。

T:插入 | 源 CriticMarkup  
预期 标记内容显示为新增，通常带下划线或绿色 | 流行度 B

The sentence has {++an inserted clause++} inside it.

T:删除 | 源 CriticMarkup  
预期 标记内容显示为删减，通常带删除线或红色 | 流行度 B

The sentence has {--a deleted clause--} inside it.

T:替换 | 源 CriticMarkup  
预期 旧内容显示为删除、新内容显示为插入 | 流行度 B

The value is {~~old wording~>new wording~~} after the change.

T:高亮 | 源 CriticMarkup  
预期 标记内容带高亮背景 | 流行度 B

The phrase {==highlighted phrase==} should draw attention.

T:注释 | 源 CriticMarkup  
预期 标记内容作为批注呈现 | 流行度 C

This needs review {>>check the wording here<<} before publishing.

T:三种定界符对照 | 源 跨语法对照  
预期 删除线、Pandoc 高亮、CriticMarkup 高亮三者外观可区分 | 流行度 C

Strikethrough uses ~~text~~, Pandoc highlight uses ==text==, and CriticMarkup uses {==text==}.

T:嵌套标记 | 源 CriticMarkup 嵌套  
预期 内外两层各自生效 | 流行度 C

The line {~~keep {==important==} words~>replace them~~} shows nesting.

T:未闭合标记 | 源 CriticMarkup 边界  
预期 花括号原样显示，不吞掉后续内容 | 流行度 C

Here is an {++unclosed insertion marker and the text after it stays visible.
