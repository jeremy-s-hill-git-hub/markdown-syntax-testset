# 素材来源（已核实）

写用例需要引用规范章节、或需要确认某条语法的出处时读本文件。

## 规范原文

`_sources/` **不入版本库**（见 `.gitignore`）。若本地缺失，按下表的位置与来源重新获取；无法获取时按 `agent-rules.md` 的 A7 规则向用户请求，**不得凭记忆填充判断**。

| 方言 | 素材 | 位置 | 状态 |
| --- | --- | --- | --- |
| CommonMark 0.31.2 | `spec.txt` 完整规范 | `_sources/spec.txt` | 完整，9814 行 |
| GFM 0.29-gfm | 规范 HTML | `_sources/GitHub Flavored Markdown Spec.html` | 完整 |
| Pandoc | 手册 HTML（含扩展默认状态） | `_sources/Pandoc - Pandoc User's Guide.html` | 完整 |
| Pandoc | 程序自述（**权威**） | `pandoc --list-extensions=markdown` | 73 条 |

**交叉验证结论**：HTML 手册与程序输出在 72 个共有扩展上判定**完全一致**，零冲突。

判断「Pandoc 是否默认支持某扩展」时以**程序输出**为准，不以手册或纯文本为准——抓取所得纯文本可能丢失标记（如 `±` 兼作 `+`/`-`）。

## 编辑器特性与其他方言

多为编辑器行为或分散规范，非单一规范文本，以「可观察的渲染结果」为准。

| 主题 | 参考来源 |
| --- | --- |
| Mermaid | mermaid.js.org 文档；GitHub Docs「Creating diagrams」 |
| GitHub Alerts | GitHub Docs（Alerts 语法） |
| CriticMarkup | criticmarkup.com |
| MultiMarkdown | MultiMarkdown v6 规范 |
| Markdown Extra | michelf.ca/projects/php-markdown/extra |
| Kramdown | kramdown 规范 |

## CommonMark 章节号

以 `spec.txt` 实际行序为准，**勿凭记忆**。

| 章节 | 行号 |
| --- | --- |
| §4.1 Thematic breaks | 875 |
| §4.2 ATX headings | 1099 |
| §4.3 Setext headings | 1321 |
| §4.4 Indented code blocks | 1737 |
| §4.5 Fenced code blocks | 1937 |
| §4.6 HTML blocks | 2363 |
| §4.7 Link reference definitions | 3184 |
| §4.8 Paragraphs | 3539 |
| §4.9 Blank lines | 3649 |
| §5.1 Block quotes | 3693 |
| §5.2 List items | 4122 |
| §5.3 Lists | 5241 |
| §6.1 Code spans | 5890 |
| §6.2 Emphasis | 6123 |
| §6.3 Links | 7487 |
| §6.4 Images | 8557 |
| §6.5 Autolinks | 8784 |
| §6.6 Raw HTML | 8971 |
| §6.7 Hard line breaks | 9247 |
| §6.8 Soft line breaks | 9397 |
| §6.9 Textual content | 9432 |

## 素材获取

材料无法自行获取时，按 `agent-rules.md` 的 A7 规则向用户请求，不得凭记忆填充。用户提供后须读回验证，并说明实际拿到什么、缺什么。
