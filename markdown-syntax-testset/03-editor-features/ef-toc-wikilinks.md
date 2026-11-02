# 自动目录与 WikiLinks

本文件测试两种常见的编辑器特性：自动目录占位符与 WikiLinks。
二者都不是 Markdown 规范语法，未支持时按原文显示。
示例文字一律用英文，说明文字用中文。
注：Kramdown 的自动目录由 `toc_levels` 选项控制，其标记写法本集未纳入测试；本文件只测编辑器常见的方括号形式。

## 自动目录

T:方括号形式 | 源 编辑器约定  
预期 展开为本文档的目录 | 流行度 B

[TOC]

T:双方括号形式 | 源 编辑器约定  
预期 部分编辑器展开为目录，否则原样显示 | 流行度 C

[[toc]]

## WikiLinks

T:基本链接 | 源 Obsidian 等编辑器约定  
预期 渲染为指向同名页面的链接 | 流行度 A

See [[Project Notes]] for details.

T:带别名 | 源 编辑器约定  
预期 显示别名文字，跳转目标为页面名 | 流行度 B

See [[Project Notes|the notes page]] for details.

T:内容嵌入 | 源 编辑器约定  
预期 内联嵌入目标页面内容 | 流行度 B

![[Embedded Page]]

T:目标页面不存在 | 源 编辑器约定  
预期 显示为可创建的新链接或保留原文 | 流行度 C

See [[Page That Does Not Exist]] in the notes.

T:列表与引用内 | 源 结构组合  
预期 链接在列表项与引用块内正常渲染 | 流行度 C

- An item linking to [[Project Notes]]
- Another item

> A quote linking to [[Project Notes]]
