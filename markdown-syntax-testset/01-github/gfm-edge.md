# GFM 与 CommonMark 的差异

本文件逐条对照 GFM 与 CommonMark 的行为分歧。
每条只演示**差异点本身**，共有的语法不在此重复。

GFM 自我声明为 CommonMark 的**严格超集**，因此理论上不应有冲突。
实际上仍有若干处：或因为 GFM 定格在 CommonMark 0.29，或因为扩展改变了原有语义。

示例文字一律用英文，说明文字用中文。

## 版本滞后

CommonMark 0.31.2 明确规定文档开头的字节顺序标记应被忽略；GFM 规范全文未提及字节顺序标记。因此同一份带字节顺序标记的文件，按 CommonMark 应无差异，按 GFM 则无据可依，预期输出取决于实现，本条不作断言。

#### T:文档开头的 BOM 是否被忽略 | 源 CM 0.31.2 第 2.1 节 / GFM 无规定 | 预期 规范层面存疑，实现可能不一致

## 表格

CommonMark 不认识表格的对齐分隔行，会把它当作普通文字行；GFM 则把「表头 + 分隔行 + 数据行」识别为表格。差别在于块的边界：同一段文字在两种规范下可能得到不同的块划分。此外 GFM 中表格遇到空行或其他块级结构即终止。

T:表格在 CommonMark 中的归属 | 源 CM 0.31.2 无表格 / GFM 0.29-gfm 第 4.10 节  
预期 按 CommonMark 渲染时表格不成形 | 流行度 A

| Column one | Column two |
| --- | --- |
| Alpha | Beta |

上面这段若按 CommonMark 解析，不是表格，而是若干段落。
差别在于：CommonMark 不认识分隔行，会把它当作普通文字行。

T:表格不能被其他块打断的边界 | 源 GFM 0.29-gfm 第 4.10 节  
预期 引用块终止表格 | 流行度 B

| Column one | Column two |
| --- | --- |
| Alpha | Beta |

> This paragraph is outside the table.

## 任务列表

关键差异是：任务列表不是新语法，而是对列表项内容的二次处理。方括号在 CommonMark 中只是普通字符，在 GFM 中被升级为复选框标记；且标记必须位于项内首个块的开头。

T:任务项与普通列表项的差别 | 源 GFM 0.29-gfm 第 5.3 节  
预期 前三项带复选框，后两项为纯文字 | 流行度 A

- [ ] Checkbox, unchecked
- [x] Checkbox, checked
- [X] Uppercase also works
- A plain list item has no checkbox
- [y] Not a space and not x, so not a task item

T:任务标记必须位于项内首个块的开头 | 源 GFM 0.29-gfm 第 5.3 节  
预期 第二项不生成复选框 | 流行度 C

- [x] Marker at the start of the item, checkbox appears

- A paragraph comes first, [ ] so this marker is not a task item

## 删除线

CommonMark 只把星号与下划线定义为强调定界符，波浪线在 CommonMark 中是完全的中性字符；GFM 则赋予它删除线含义。因此同一行波浪线在两者中结果不同。

T:波浪线在 CommonMark 中无特殊含义 | 源 CM 0.31.2 / GFM 0.29-gfm 第 6.5 节  
预期 按 CommonMark 显示原文，按 GFM 显示删除线 | 流行度 A

~~Four tildes around this line: literal text in CommonMark, strikethrough in GFM~~

T:单波浪线的归属 | 源 GFM 0.29-gfm 第 6.5 节  
预期 单个波浪线也产生删除线 | 流行度 B

~A single tilde also produces strikethrough in GFM~

T:删除线与强调的定界符不冲突 | 源 GFM 0.29-gfm 第 6.5 节  
预期 两者同时生效，互不干扰 | 流行度 B

**Bold containing ~~strikethrough~~ still works**

CommonMark 的星号定界符与 GFM 的波浪线定界符分属两套，正常情况下不会互相抢占。

## 自动链接

尖括号自动链接在两者中都成立，区别在于 GFM 额外允许省略尖括号：裸 URL、`www.` 前缀与裸邮箱都会被识别，且触发位置受限。

T:尖括号自动链接在两者中都成立 | 源 CM 0.31.2 第 6.5 节 / GFM 0.29-gfm 第 6.8 节  
预期 两者均渲染为链接 | 流行度 A

<https://example.com/angle>

T:无尖括号时 GFM 才识别 | 源 CM 0.31.2 不支持 / GFM 0.29-gfm 第 6.9 节  
预期 按 CommonMark 是纯文字，按 GFM 是链接 | 流行度 A

https://example.com/no-angle

T:www 前缀是 GFM 独有的自动补全 | 源 GFM 0.29-gfm 第 6.9 节  
预期 GFM 补全协议头，CommonMark 不识别 | 流行度 A

www.example.com

T:裸邮箱只在 GFM 中自动链接 | 源 CM 0.31.2 不支持 / GFM 0.29-gfm 第 6.9 节  
预期 CommonMark 显示纯文字，GFM 生成 mailto | 流行度 A

someone@example.com

T:自动链接的触发位置限制 | 源 GFM 0.29-gfm 第 6.9 节  
预期 紧贴前文时不触发 | 流行度 C

textwww.example.comdoes not trigger

## 原始 HTML 的过滤

这是两者最实质的分歧：CommonMark 要求原始 HTML 不经转义直接输出，安全性交给实现方；GFM 则内置标签过滤器，把九个特定标签的开头尖括号改写为实体，使其显示为文字。

T:普通标签在两者中都直通 | 源 CM 0.31.2 第 6.10 节 / GFM 0.29-gfm 第 6.10 节  
预期 两者均渲染为实际元素 | 流行度 A

<strong>This text should render bold</strong>

T:危险标签在 CommonMark 中不被过滤 | 源 CM 0.31.2 不过滤 / GFM 0.29-gfm 第 6.11 节  
预期 CommonMark 原样输出，GFM 转义后显示为文字 | 流行度 A

<script>In CommonMark this is emitted as is; in GFM it is escaped</script>

T:过滤只针对九个特定标签 | 源 GFM 0.29-gfm 第 6.11 节  
预期 iframe 被过滤，其余块级标签不受影响 | 流行度 B

<iframe src="https://example.com"></iframe>

<details>This tag is not on the filter list and should be preserved</details>

被过滤的九个标签是：title、textarea、style、xmp、iframe、noembed、noframes、script、plaintext。名单之外一律不动。

T:过滤方式是把尖括号改写为实体 | 源 GFM 0.29-gfm 第 6.11 节  
预期 该行显示为可见的文字，而不是空段落 | 流行度 B

<style>This will be escaped into visible text</style>

## 文档结构层面的分歧

差异不在文字，而在块的边界；测量时应同时观察文字是否可见与块是否成形。GFM 声明自己是 CommonMark 的严格超集，但前面的用例表明这一声明在实现层面未必成立。

T:两种规范对同一文档的块结构判定 | 源 综合  
预期 同一段文字在两种规范下可能得到不同的块划分 | 流行度 C

| Looks like a table |
| --- |
| In CommonMark these three lines are separate paragraphs |

T:规范的自我声明 | 源 GFM 0.29-gfm 第 1.1 节  
预期 说明文字本身也是样例 | 流行度 B

GFM 声明自己是 CommonMark 的严格超集。
严格超集的含义是：任何合规的 CommonMark 文档在 GFM 下也应合规。
上面这句说明本身就是一个普通段落，因此它同时也是段落的样例。
