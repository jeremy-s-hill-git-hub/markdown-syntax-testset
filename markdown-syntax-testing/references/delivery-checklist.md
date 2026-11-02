# 交付检查清单

**仅当用户宣布进入最终交付时执行以下全部步骤。全部步骤只针对最终产物文件夹 `markdown-syntax-testset/`。**

## 第 0 步 · 确认无重复副本

测试文件只应存在于 `markdown-syntax-testset/` 一处，不再有工作副本。在 `markdown/` 下执行：

```
find . -name 'cm-block.md' -not -path './markdown-syntax-testset/*'
```

预期：**无输出**。若命中，说明存在重复副本，须先确认哪份为准并删除另一份。

`_sources/`（素材、脚本、skill 历史版本）与 `markdown-syntax-testing/`（skill 包）始终位于该目录之外，属正常存在。

## 第 1 步 · 最终产物文件夹内的残留检查

```
find markdown-syntax-testset \( -name '*.py' -o -name '*.sh' -o -name '*.txt' -o -name '*.html' -o -name '_sources' \)
```

只检查最终产物文件夹，**不检查工作区**——工作区内的脚本与素材属正常存在。

预期：**无输出**。

## 第 2 步 · 顶层白名单核对

```
ls -la markdown-syntax-testset
```

预期：仅 `README.md` + `00-commonmark/` + `01-github/` + `02-pandoc/` + `03-editor-features/` + `04-other-dialects/`。

## 第 3 步 · README 链接全解析与双向互证

- 取出 `README.md` 里所有相对链接目标（排除 `#` 开头的锚点），逐个确认目标文件真实存在；
- 反过来，目录里每个测试文件都必须被 README 列出。

预期：**两个方向都无遗漏**。

## 第 4 步 · 文件完整性

| 检查 | 预期 |
| --- | --- |
| 每个文件 H1 计数 | 1（`cm-block.md` 为 2，第二个是一级标题用例的被测对象） |
| 残留章节符 `§` | 0 |
| 每个 `##` 主题 | 以中文规则段开头，再列用例 |
| 草稿残留 `[T]` | 0 |
| 用例数与标签数 | 每个 `T:` 标签都有对应被测量对象，无孤立标签 |
| 版本号 | 工作区 `README.md` 与 `SKILL.md` 一致（当前 2.0.0） |

## 第 5 步 · 围栏配对

预期：所有围栏平衡；唯一允许的未闭合是「未闭合」类用例本身，且**全部位于所属文件的最末**。

当前允许的未闭合用例（自前至后）：

| 文件 | 未闭合用例 |
| --- | --- |
| `cm-block.md` | 未闭合强调、未闭合的方括号、未闭合围栏吞掉文件余下内容 |
| `cm-inline.md` | 未闭合自动链接、未闭合代码跨度不跨空行、未闭合定界符当原文 |
| `cm-edge.md` | 未闭合星号强调、未闭合下划线强调、未闭合代码跨度、未闭合链接方括号、未闭合链接圆括号、未闭合图片、未闭合 HTML 标签、未闭合围栏吞掉余下内容 |
| `cm-eof.md` | 未闭合 HTML 注释吞到文件末尾 |
| `gfm-ext.md` | 未闭合波浪线按原文 |
| `gh-ext.md` | 未闭合围栏吞掉余下内容 |
| `ef-critic.md` | 未闭合标记 |

`cm-edge.md` 与 `gh-ext.md` 末尾的未闭合围栏之后即为文件结尾；`cm-block.md` 的未闭合围栏同样收尾。

`cm-eof.md` 的未闭合 HTML 注释会吞掉其后全部内容，因此该文件仅此一条吞噬型用例，其余用例全部排在它之前。

`cm-edge.md` 的未闭合围栏使用 `~~~text` 而非反引号，意在避开与同文件「未闭合代码跨度」的反引号冲突，属有意设计。

若任一未闭合用例之后出现任何内容，即为缺陷。

## 第 6 步 · 维度归属核对

| 维度 | 目录 | 预期文件 |
| --- | --- | --- |
| CommonMark | `00-commonmark/` | `cm-block`、`cm-inline`、`cm-edge`、`cm-eof` |
| GitHub | `01-github/` | `gfm-ext`、`gfm-edge`、`gh-ext` |
| Pandoc | `02-pandoc/` | `pd-on-block`、`pd-on-inline`、`pd-on-table`、`pd-off-block`、`pd-off-inline` |
| 编辑器特性 | `03-editor-features/` | `ef-critic`、`ef-toc-wikilinks` |
| 其他方言 | `04-other-dialects/` | `od-other` |

**同一语法只应在一个维度出现**；数学、脚注、emoji、Alerts、Mermaid 应仅出现在 `01-github/gh-ext.md`。

## 第 7 步 · 安全提示

含裸 `<script>` / `<iframe>` / `<style>` 的用例：

| 文件 | 用例 |
| --- | --- |
| `gfm-ext.md` | 危险标签被替换、iframe 被过滤、style 标签被过滤、大小写不影响过滤 |
| `gfm-edge.md` | 危险标签在 CommonMark 中不被过滤、过滤只针对九个特定标签、过滤方式是把尖括号改写为实体 |

另：`gh-ext.md` 的 Mermaid 图表由活动的 JavaScript 渲染。交付时须提醒使用者：**先看源码视图，再切预览**；无法确认编辑器安全策略时，使用隔离环境。

## 第 8 步 · 提交

- 主要交付物 = `markdown/markdown-syntax-testset/` 目录整体。
- 开发工作区 `markdown/` 保留不动，含 `_sources/`、脚本与后续迭代产物。

---

# 执行流程

1. 按 `project-rules.md` 的目录结构建立工作区与内容目录 `markdown-syntax-testset/`。
2. 逐文件产出测试内容（先 CommonMark → GitHub → Pandoc，再 03-editor-features → 04-other-dialects）。
3. 逐文件自检：裸露性、规则段、自我一致性、未闭合风险、标题层级、语言分工、跨维度去重。
4. 最后写 `README.md`（它是索引与说明，需等子文件齐备后才能写全）。
5. 用户目测确认。
6. 用户宣布交付 → 执行本文件第 0–8 步做确认性核对。因测试文件只有一份，正常情况下应当一次通过。
