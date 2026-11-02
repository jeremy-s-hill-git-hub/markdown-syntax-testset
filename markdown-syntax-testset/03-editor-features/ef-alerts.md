# GitHub Alerts

本文件测试 GitHub Alerts（块引用中以类型标记开头的扩展）。
被测对象是引用块是否被识别为带图标的提示框，还是退化为普通引用。
示例文字一律用英文，说明文字用中文。

## 五种类型

T:NOTE | 源 GitHub Alerts  
预期 带信息图标的提示框 | 流行度 A

> [!NOTE]
> Useful information that users should know.

T:TIP | 源 GitHub Alerts  
预期 带建议图标的提示框 | 流行度 A

> [!TIP]
> A helpful piece of advice.

T:IMPORTANT | 源 GitHub Alerts  
预期 带重要标记的提示框 | 流行度 B

> [!IMPORTANT]
> Information the user must not miss.

T:WARNING | 源 GitHub Alerts  
预期 带警告图标的提示框 | 流行度 B

> [!WARNING]
> Something that needs immediate attention.

T:CAUTION | 源 GitHub Alerts  
预期 带危险图标的提示框 | 流行度 B

> [!CAUTION]
> A negative consequence is possible.

## 边界

T:小写与无效类型 | 源 GitHub Alerts 大小写敏感  
预期 小写可能不生效，无效类型退化为普通引用 | 流行度 C

> [!note]
> Lowercase may not render as an alert.

> [!UNKNOWN]
> An unknown type becomes a plain block quote.

T:内含行内语法 | 源 结构组合  
预期 粗体与行内代码在提示框内生效 | 流行度 B

> [!TIP]
> Run `git status` to see **modified files**.

T:标记不在引用首行 | 源 位置条件  
预期 不识别为 alert，按普通引用显示 | 流行度 C

> Some text appears before the marker.
> [!NOTE]
> This does not start with the marker.
