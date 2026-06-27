import re, os

base = r'd:\网站建设\网址导航\amzrover.cn\en'
counts = {}
total = 0
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            with open(fp, encoding='utf-8') as fh:
                c = 0
                for line in fh:
                    c += len(re.findall(r'[\u4e00-\u9fff]', line))
            if c > 0:
                rel = os.path.relpath(fp, base)
                counts[rel] = c
                total += c

for k, v in sorted(counts.items(), key=lambda x: -x[1]):
    print(f"{k}: {v} Chinese chars")
print(f"\nTotal: {total} Chinese chars in {len(counts)} files")
