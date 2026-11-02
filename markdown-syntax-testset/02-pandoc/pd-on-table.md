# Pandoc 默认开启的扩展·表格

本文件测试 Pandoc 默认开启的表格扩展。管道表格与 GFM 兼容，已归 GitHub 维度，见 `01-github/gfm-ext.md`；此处只收 Pandoc 独有的简单表格、多行表格、网格表格与表格题注。

示例文字一律用英文，说明文字用中文。

## 简单表格

简单表格用一行文字加下划线与短横线分隔表头与数据，列宽由分隔行的位置决定。

T:简单表格 | 源 PM simple_tables  
预期 渲染为表格 | 流行度 B

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123

## 多行表格

多行表格允许单元格内容跨行，行与行之间用空行分隔。

T:多行表格 | 源 PM multiline_tables  
预期 单元格内容可跨行 | 流行度 C

-------------------------------------------------------------
 Centered   Default           Right Left
  Header    Aligned         Aligned Aligned
----------- ------- --------------- -------------------------
   First    row                12.0 Example of a row that
                                    spans multiple lines.

  Second    row                 5.0 Here is another one. Note
                                    the blank line between
                                    rows.
-------------------------------------------------------------

## 网格表格

网格表格用加号、减号与竖线画出完整边框，可跨行列合并。

T:网格表格 | 源 PM grid_tables  
预期 渲染为带边框的表格 | 流行度 C

+---------------+---------------+
| Fruit         | Price         |
+===============+===============+
| Bananas       | $1.34         |
+---------------+---------------+

## 表格题注

在表格下方写一行冒号起头的文字，即为表格题注。

T:表格标题 | 源 PM table_captions  
预期 表格下方出现题注 | 流行度 B

| Variety | Price |
|---------|------:|
| Apple   |  3.00 |

: Fruit price table
