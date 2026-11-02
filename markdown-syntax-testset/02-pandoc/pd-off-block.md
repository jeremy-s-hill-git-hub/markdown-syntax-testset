# Pandoc 默认关闭的扩展·块级

本文件测试 Pandoc 的 `markdown` 格式下默认不生效、且属于块级的扩展。
这些语法在默认状态下按纯文本处理；在格式名后追加 `+扩展名` 后才生效。
行内关闭项见 `pd-off-inline.md`，默认开启项见 `pd-on-block.md`。
示例文字一律用英文，说明文字用中文。

## 四空格规则

默认采用标记宽度判定列表续行缩进；开启 four_space_rule 后一律要求四空格。

T:列表续行的缩进判定 | 源 PM four_space_rule  
预期 默认按标记宽度判定，开启后一律要求四空格 | 流行度 C

- The first paragraph of the item

  A continuation paragraph indented by two spaces

## 无空行的列表

默认要求列表前有空行；开启 lists_without_preceding_blankline 后，紧贴段落的减号行也会被识别为列表。

T:列表紧接段落而无需空行 | 源 PM lists_without_preceding_blankline  
预期 默认不作为列表，开启后成为列表 | 流行度 C

The line above is a paragraph.
- By default this line does not start a list

## 紧凑定义列表

开启 compact_definition_lists 后，定义列表的各项之间无需空行也能保持紧凑。

T:紧凑定义列表 | 源 PM compact_definition_lists  
预期 默认松散，开启后紧凑 | 流行度 D

Term

:   Definition

Another term

:   Another definition

## Markdown 属性

开启 markdown_attribute 后，可用 markdown 属性控制是否在标签内解析 Markdown。

T:标签上的 markdown 属性 | 源 PM markdown_attribute  
预期 默认不解析，开启后按属性值决定 | 流行度 C

<div markdown="1">
*This text may or may not be parsed as markdown.*
</div>

## MultiMarkdown 标题块

开启 mmd_title_block 后，Pandoc 识别 MultiMarkdown 风格的标题块，即文件开头以 key: value 起头的几行。

T:MMD 标题块 | 源 PM mmd_title_block  
预期 默认按正文显示，开启后被提取 | 流行度 D

Title: An MMD style title
Author: Example Author

Body text after the title block.

## MMD 标题标识符

开启 mmd_header_identifiers 后，标题末尾的方括号会被当作标识符。

T:MMD 标题标识符 | 源 PM mmd_header_identifiers  
预期 默认显示方括号原文，开启后成为锚点 | 流行度 D

### A heading with an MMD identifier [mmd-anchor]

## 文学式 Haskell

开启 literate_haskell 后，把源码按文学式 Haskell 处理，非代码部分作为正文。

T:文学式 Haskell | 源 PM literate_haskell  
预期 默认按普通 Markdown，开启后按文学程序处理 | 流行度 D

This paragraph is ordinary markdown by default; with literate_haskell it is treated as prose.
