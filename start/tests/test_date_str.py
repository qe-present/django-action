import regex  # 注意：Python 标准库 re 不支持递归，用第三方 regex 模块

s = '(SINCE 4-Oct-2025 BEFORE 4-Oct-2025)'
pattern = regex.compile(r'(?<content>(?<rec>\((?:[^()]++|(?&rec))*\)))')

for m in pattern.finditer(s):
    print(m.group('content')[1:-1])