"""Markdown 测试样本集自检脚本（v2）。

在开发工作区根目录（markdown/）下执行：
    python markdown-syntax-testing/scripts/audit.py

检查项：
- 每个文件的行数、用例数、围栏平衡、H1 计数
- 残留章节符（U+00A7）
- 每个 `##` 主题是否以规则段开头（仅子文件）
- README 是否覆盖 B5 九项基础语法
- skill 与测试集版本是否一致
- 行首围栏型危险行
"""

import re
import glob
import os

ROOT = 'markdown-syntax-testset'
SKILL = 'markdown-syntax-testing/SKILL.md'
WS_README = 'README.md'
SEC = '\u00a7'

subfiles = sorted(glob.glob(f'{ROOT}/0*/*.md'))
readme = f'{ROOT}/README.md'
files = subfiles + ([readme] if os.path.exists(readme) else [])

CASE = re.compile(r'^(?:#{1,6} )?T:')
H2 = re.compile(r'^## ')

print(f"{'file':40s} {'lines':>6s} {'cases':>6s} {'fence':>9s} {'H1':>4s}")
print('-' * 72)

total = 0
for p in files:
    txt = open(p, encoding='utf-8').read()
    lines = txt.split('\n')
    cases = len(re.findall(r'(?m)^(?:#{1,6} )?T:', txt))
    total += cases

    fence = None
    op = None
    for i, l in enumerate(lines, 1):
        m = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', l)
        if not m:
            continue
        ch, ln = m.group(1)[0], len(m.group(1))
        if fence is None:
            fence, op = (ch, ln), i
        elif ch == fence[0] and ln >= fence[1]:
            fence = None
    fstat = 'OK' if fence is None else f'OPEN@{op}'
    h1 = sum(1 for l in lines if re.match(r'^# ', l))
    print(f'{p:40s} {len(lines):6d} {cases:6d} {fstat:>9s} {h1:4d}')

print('-' * 72)
print(f'合计用例：{total}')

# 1) 残留章节符
print('\n=== 残留章节符（U+00A7）===')
hits = [(p, i) for p in files
        for i, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1)
        if SEC in l]
print('  无' if not hits else '\n'.join(f'  {p}:{i}' for p, i in hits))

# 2) 规则段检查（仅子文件）
print('\n=== 缺规则段的 `##` 主题（仅子文件）===')
missing = []
for p in subfiles:
    lines = open(p, encoding='utf-8').read().split('\n')
    for i, l in enumerate(lines):
        if not H2.match(l):
            continue
        # 只为中文主题标题做规则段检查；英文 `##` 行是被测的 ATX 标题对象
        if not re.search(r'[\u4e00-\u9fff]', l):
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines) or CASE.match(lines[j]) or re.match(r'^#{3,6} ', lines[j]):
            missing.append(f'{p}:{i + 1}  {l[3:].strip()}')
print('  无' if not missing else '\n'.join(f'  {m}' for m in missing))

# 3) README 九项覆盖
print('\n=== README 基础语法九项覆盖 ===')
ITEMS = ['段落', '标题', '无序列表', '有序列表', '引用', '分隔线', '强调', '行内代码', '链接']
if os.path.exists(readme):
    r = open(readme, encoding='utf-8').read()
    for it in ITEMS:
        print(f'  {"OK  " if ("### " + it) in r else "MISS"}  {it}')
else:
    print('  README.md 不存在')

# 4) 版本一致性
print('\n=== 版本一致性 ===')
skill_v = ws_v = None
if os.path.exists(SKILL):
    m = re.search(r'(?m)^version:\s*"?([^"\n]+)"?', open(SKILL, encoding='utf-8').read())
    skill_v = m.group(1).strip() if m else None
if os.path.exists(WS_README):
    m = re.search(r'版本[:：]\s*([0-9][0-9.]*)', open(WS_README, encoding='utf-8').read())
    ws_v = m.group(1).strip() if m else None
print(f'  skill:   {skill_v}')
print(f'  testset: {ws_v}')
print('  ' + ('一致' if skill_v == ws_v else '不一致'))

# 5) 行首围栏型危险行
print('\n=== 行首围栏型危险行（3+ 反引号或波浪线）===')
for p in files:
    for i, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
        if re.match(r'^ {0,3}(`{3,}|~{3,})', l):
            print(f'  {p}:{i}  {l[:50]}')
