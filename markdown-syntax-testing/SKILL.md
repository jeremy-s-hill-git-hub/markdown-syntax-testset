---
name: markdown-syntax-testing
description: "构建并维护 Markdown 语法支持范围测试样本集：面向目标编辑器，用裸露（不被代码块包裹）的语法片段肉眼判断 CommonMark / GitHub（GFM 规范与 GitHub 非规范扩展）/ Pandoc 及编辑器特性的支持情况。交付物兼具说明文档与测试文档双重身份。当需要为某个编辑器建立语法支持清单、为读者提供可读的语法样例、或修订既有测试样本集时使用。"
version: "2.0.0"
---

# Markdown 语法测试样本集

## 用途

产出可直接在目标编辑器中打开、**肉眼目测** 的 Markdown 样本文件，用于判断该编辑器对各类 Markdown 语法的支持情况。

交付物具有**二重身份**：既是说明文档，也是测试文档。解释必然举例，举例必然渲染，因此「说明即测试」——写「这是一个段落」的那段话，本身就是一个段落，也同时验证了段落渲染。

覆盖面底线：至少包括 CommonMark、GitHub（含 GFM 规范与 GitHub 非规范扩展）。

## 维度与归属

测试按平台 / 引擎划分五个维度，每个语法只归其所有者测试一次（完整定义见 `references/project-rules.md` 的 B1.1）：

| 维度 | 目录 | 子部分 |
| --- | --- | --- |
| CommonMark | `00-commonmark/` | 规范主体（`cm-block`/`cm-inline`）+ 边界异常（`cm-edge`/`cm-eof`） |
| GitHub | `01-github/` | GFM 规范（`gfm-*`）+ GitHub 非规范（`gh-*`） |
| Pandoc | `02-pandoc/` | 默认开启（`pd-on-*`）+ 默认关闭（`pd-off-*`） |
| 编辑器特性 | `03-editor-features/` | CriticMarkup、自动目录 / WikiLinks |
| 其他方言 | `04-other-dialects/` | `od-other` |

数学、脚注、emoji、Alerts、Mermaid 归 GitHub 维度，不在 Pandoc 重复。

## 何时使用

- 为某个编辑器 / 渲染器建立 Markdown 语法支持清单；
- 修订、扩充既有测试样本集；
- 需要判断某条语法属于哪个维度（CommonMark / GitHub / Pandoc / 其他）。

不适用：需要程序化解析 Markdown 的场景（本 skill 只产出供人眼判断的样例）。

## 六条硬约束

违反任一条即视为产出不合格，细节见 `references/project-rules.md`。

1. **裸露** —— 被测语法必须裸露，代码块包裹即视为未测试。
2. **无编号** —— 标签形如 `T:用例名称 | 源 规范+章节`，`T:` 后直接接名称，项目内不设编号；章节写法禁用 `§`，数字写 `第 X.Y 节`，命名扩展直接写扩展名。
3. **语言分工** —— 说明文字用中文，示例文字用英文；被测量对象本身是中文时例外，需就近注明理由。
4. **未闭合置末** —— 全部未闭合构造放在文件末尾，按吞噬范围递增排列，未闭合围栏居最末且之后不得有任何内容。
5. **位置敏感** —— YAML 元数据块、传统标题块只在文档最开头生效，必须让出文件前几行。
6. **不记录** —— 不写自检结果、测试结果、汇总表、历史对比；样本集只提供「可看的语法」。

## 工作区与交付

```
markdown/
├── README.md                  ← 指向测试集 README.md
├── markdown-syntax-testset/   ← 唯一内容目录，同时是主要交付物
├── markdown-syntax-testing/   ← 本 skill 包
└── _sources/                  ← 规范原文、素材、脚本、skill 历史版本
```

测试文件**只存在一份**，位于 `markdown-syntax-testset/`，不设工作副本。因此该目录既是编辑对象也是交付物，任何时候都只能包含测试文件、`README.md` 与配套媒体这三类内容——相当于「始终处于可交付状态」，无需交付前的重建或清理。

## 工作流

1. **确认范围** —— 确定目标维度、是否含 GitHub 非规范项，以及交付边界。
2. **备料** —— 规范原文落实到 `_sources/`；无法自行获取时按 `references/agent-rules.md` 的 A7 规则向用户请求，不得凭记忆填充。
3. **写测试文件** —— 先 CommonMark，再 GitHub（GFM 规范 → GitHub 非规范）、Pandoc，最后编辑器特性与其他方言。按 B1.1 单一归属，不重复测同一语法；标签形态、文件命名与拆分见 `references/project-rules.md`。
4. **自检** —— 裸露性、自我一致性、未闭合位置、标题层级、语言分工、跨维度去重；跑 `scripts/audit.py` 核对用例数、围栏状态与 § 残留。
5. **写 README** —— 子文件齐备后再写，它承载子文件说明与基础语法样例（B4），不写使用说明或汇总。
6. **交付** —— 用户宣布交付后，按 `references/delivery-checklist.md` 的步骤做确认性核对。测试文件只有一份，正常情况下应当一次通过。

## 参考文件

按需读取，不必全部加载。

| 文件 | 何时读 |
| --- | --- |
| `references/agent-rules.md` | 涉及停手判断、写入纪律、事实核验、素材请求、安全提示时 |
| `references/project-rules.md` | 写测试文件或 README 时；含标签形态、维度归属、文件结构、各条硬约束的完整定义 |
| `references/delivery-checklist.md` | 用户宣布交付时；含核对清单与执行流程 |
| `references/sources.md` | 需要引用规范章节号、确认素材来源、判断交付白名单边界时 |

## 脚本

在 `markdown/` 下执行：

```
python markdown-syntax-testing/scripts/audit.py
```

输出每个文件的行数、用例数、围栏平衡状态、H1 计数与末行内容，并列出所有行首围栏型危险行与残留的 `§`。脚本扫描 `markdown-syntax-testset/0*/*.md` 与 `README.md`。

判读要点：`OPEN@` 开头的围栏状态若出现在 `cm-block.md`、`cm-edge.md`、`gh-ext.md` 末尾属正常（那是未闭合围栏用例本身），出现在其他文件或其他位置即为缺陷。

## 附属资源

`assets/placeholder.svg` 是图片用例必需的配套媒体，写图片相关用例时复制到测试文件的 `media/` 目录下。
