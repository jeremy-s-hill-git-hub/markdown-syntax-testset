# 素材来源（已核实）

写用例需要引用规范章节、或需要确认某条语法的出处时读本文件。

## 规范原文

`_sources/` **不入版本库**（见 `.gitignore`）。若本地缺失，按下表的位置与来源重新获取；无法获取时按 `agent-rules.md` 的 A7 规则向用户请求，**不得凭记忆填充判断**。

| 方言 | 素材 | 位置 | 状态 |
| --- | --- | --- | --- |
| CommonMark 0.31.2 | `spec.txt` 完整规范 | `_sources/spec.txt` | 完整，9814 行 |
| GFM 0.29-gfm | 规范 HTML | `_sources/GitHub Flavored Markdown Spec.html` | 完整 |
| Pandoc | 手册 HTML（含扩展默认状态） | `_sources/Pandoc - Pandoc User's Guide.html` | 完整 |
| Pandoc | 程序输出快照（**权威**） | `_sources/_bin_ext.txt` | 73 条（46 开 / 27 关） |
| Pandoc | 程序自述（可复现） | `pandoc --list-extensions=markdown` | 以本机实际输出为准 |

**交叉验证结论**：HTML 手册与程序输出在 72 个共有扩展上判定**完全一致**，零冲突（脚本 `_sources/_crosscheck.py`）。

判断「Pandoc 是否默认支持某扩展」时以**程序输出**为准，不以手册或纯文本为准——抓取所得纯文本可能丢失标记（如 `±` 兼作 `+`/`-`），且手册与程序快照存在版本漂移。

**版本**：`_bin_ext.txt` 快照对应的 pandoc 版本尚未记录，须以 `pandoc --version` 的实际输出补录。

**已知差异（手册列有、程序快照无）**：`attributes`、`tex_math_gfm`、`alerts`、`sourcepos`、`table_attributes`。写入用例前须以当前 pandoc 版本核实，不得凭手册直接判定。

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
| 第 4.1 节 Thematic breaks | 875 |
| 第 4.2 节 ATX headings | 1099 |
| 第 4.3 节 Setext headings | 1321 |
| 第 4.4 节 Indented code blocks | 1737 |
| 第 4.5 节 Fenced code blocks | 1937 |
| 第 4.6 节 HTML blocks | 2363 |
| 第 4.7 节 Link reference definitions | 3184 |
| 第 4.8 节 Paragraphs | 3539 |
| 第 4.9 节 Blank lines | 3649 |
| 第 5.1 节 Block quotes | 3693 |
| 第 5.2 节 List items | 4122 |
| 第 5.3 节 Lists | 5241 |
| 第 6.1 节 Code spans | 5890 |
| 第 6.2 节 Emphasis | 6123 |
| 第 6.3 节 Links | 7487 |
| 第 6.4 节 Images | 8557 |
| 第 6.5 节 Autolinks | 8784 |
| 第 6.6 节 Raw HTML | 8971 |
| 第 6.7 节 Hard line breaks | 9247 |
| 第 6.8 节 Soft line breaks | 9397 |
| 第 6.9 节 Textual content | 9432 |

## 素材获取

材料无法自行获取时，按 `agent-rules.md` 的 A7 规则向用户请求，不得凭记忆填充。用户提供后须读回验证，并说明实际拿到什么、缺什么。
