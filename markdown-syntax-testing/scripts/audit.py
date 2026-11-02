"""Markdown 测试样本集自检脚本。

在开发工作区根目录（markdown/）下执行：
    python markdown-syntax-testing/scripts/audit.py

输出每个测试文件的行数、用例数、围栏平衡状态、H1 计数与末行内容，
并列出所有行首围栏型危险行。
"""

import re
import glob

files = sorted(glob.glob('markdown-syntax-testset/0*/*.md'))
print(f"{'file':30s} {'lines':>6s} {'cases':>6s} {'fence':>7s} {'H1':>4s} {'last':>44s}")
print('-' * 110)

total_cases = 0
for p in files:
    txt = open(p, encoding='utf-8').read()
    lines = txt.split('\n')
    n_lines = len(lines)
    cases = len(re.findall(r'(?m)^(?:#{1,6} )?T:', txt))
    total_cases += cases

    # fence 平衡
    fence = None
    op = None
    for i, l in enumerate(lines, 1):
        m = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', l)
        if not m:
            continue
        ch = m.group(1)[0]
        n = len(m.group(1))
        if fence is None:
            fence = (ch, n)
            op = i
        elif ch == fence[0] and n >= fence[1]:
            fence = None
    fstat = 'OK' if fence is None else f'OPEN@{op}'

    h1 = sum(1 for l in lines if re.match(r'^# ', l))
    # 最后一行是否为未闭合围栏内的内容
    last = lines[-2] if len(lines) > 1 and lines[-1] == '' else lines[-1]
    print(f'{p:30s} {n_lines:6d} {cases:6d} {fstat:>7s} {h1:4d} {last[:44]:>44s}')

print('-' * 110)
print(f'合计用例：{total_cases}')

# 危险行首扫描
print('\n=== 行首围栏型危险行（3+ 反引号或波浪线）===')
for p in files:
    for i, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
        if re.match(r'^ {0,3}(`{3,}|~{3,})', l):
            print(f'  {p}:{i}  {l[:50]}')
