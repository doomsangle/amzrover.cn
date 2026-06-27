import re, os, json
from collections import Counter

base = r'd:\网站建设\网址导航\amzrover.cn\en'
chars = Counter()

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.html'):
            continue
        fp = os.path.join(root, f)
        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()
        for ch in re.findall(r'[\u4e00-\u9fff]', content):
            chars[ch] += 1

# Write char frequency to file
with open(r'd:\网站建设\网址导航\amzrover.cn\char-freq.json', 'w', encoding='utf-8') as f:
    json.dump(chars.most_common(), f, ensure_ascii=False, indent=2)

print(f'Unique Chinese chars: {len(chars)}')
print(f'Total Chinese chars: {sum(chars.values())}')
